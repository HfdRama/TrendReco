document.addEventListener("DOMContentLoaded", () => {

    // =========================
    // ELEMENT
    // =========================
    const toggleBtn = document.getElementById("chat-toggle");
    const closeBtn = document.getElementById("close-chat");
    const chatBox = document.getElementById("chat-container");
    const sendBtn = document.getElementById("send-chat");
    const input = document.getElementById("chat-input");
    const body = document.getElementById("chat-body");
    const typing = document.getElementById("typing");

    // DEBUG
    console.log("Chat Loaded");

    // cek apakah semua element ditemukan
    if (
        !toggleBtn ||
        !closeBtn ||
        !chatBox ||
        !sendBtn ||
        !input ||
        !body
    ) {
        console.error("Ada element chatbot yang tidak ditemukan");
        return;
    }

    // =========================
    // OPEN CHAT
    // =========================
    toggleBtn.addEventListener("click", () => {
        chatBox.classList.toggle("hidden");
        if (!chatBox.classList.contains("hidden")) {
            input.focus();
            body.scrollTop = body.scrollHeight;
        }
    });

    // =========================
    // CLOSE CHAT
    // =========================
    closeBtn.addEventListener("click", () => {
        chatBox.classList.add("hidden");
    });

    // =========================
    // SEND BUTTON
    // =========================
    sendBtn.addEventListener("click", sendMessage);

    // =========================
    // ENTER
    // =========================
    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            sendMessage();
        }
    });

    // =========================
    // QUICK ASK
    // =========================
    window.quickAsk = function(text) {
        input.value = text;
        sendMessage();
    }

    // =========================
    // SEND MESSAGE
    // =========================
    function sendMessage() {
        const message = input.value.trim();

        if (!message) return;

        // USER BUBBLE
        body.insertAdjacentHTML(
            "beforeend",
            `
            <div class="flex justify-end animate-[fadeIn_0.2s_ease-out]">
                <div class="max-w-[85%] sm:max-w-[75%]">
                    <div class="bg-blue-600 text-white p-3.5 rounded-2xl rounded-tr-sm shadow-sm text-sm">
                        ${message}
                    </div>
                    <p class="text-[10px] text-right text-gray-400 mt-1 mr-1">sekarang</p>
                </div>
            </div>
            `
        );

        body.scrollTop = body.scrollHeight;

        input.value = "";

        if (typing) {
            typing.classList.remove("hidden");
        }

        fetch("/chatbot/send", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        })
        .then(res => res.json())
        .then(data => {

            if (typing) {
                typing.classList.add("hidden");
            }

            body.insertAdjacentHTML(
                "beforeend",
                `
                <div class="flex gap-3 animate-[fadeIn_0.2s_ease-out]">
                    <div class="w-9 h-9 rounded-xl bg-gradient-to-r from-blue-600 to-indigo-600 text-white flex items-center justify-center shrink-0 text-xs">
                        <i class="fa-solid fa-robot"></i>
                    </div>
                    <div class="max-w-[85%] sm:max-w-[75%]">
                        <div class="bg-white p-3.5 rounded-2xl rounded-tl-sm shadow-sm text-sm text-slate-700">
                            ${data.reply}
                        </div>
                        <p class="text-[10px] text-gray-400 mt-1 ml-1">sekarang</p>
                    </div>
                </div>
                `
            );

            body.scrollTop = body.scrollHeight;

        })
        .catch(error => {
            console.error(error);
            if (typing) {
                typing.classList.add("hidden");
            }
        });
    }
});