/* CHATBOT */
const chatData= [
      {
        q: "Como funciona a Chamada da Lupa?",
        a: "A Chamada da Lupa conecta você com usuários aleatórios. Ela não paga moedas, mas serve pra você puxar conversa e fazer o usuário te adicionar como amiga. Aí sim você ganha nas chamadas de Amigo!",
      },
      {
        q: "Qual chamada paga mais?",
        a: "A Chamada de Amigo é a que mais paga! Quanto mais tempo você ficar na chamada, mais moedas você ganha. O valor base é 80 moedas por minuto, podendo chegar a 120 com bom desempenho.",
      },
      {
        q: "O que fazer se o usuário me incomodar?",
        a: "Encerra a chamada na hora e denuncia pelo app. A equipe analisa e toma as medidas. Sua segurança vem primeiro!",
      },
      {
        q: "Posso usar óculos escuros na chamada?",
        a: "Não pode não! Óculos escuros, cobrir a câmera ou bloquear a tela são proibidos durante as chamadas.",
      },
      {
        q: "O que acontece se eu quebrar uma regra?",
        a: "Depende da gravidade. Pode ser um aviso, suspensão temporária ou até bloqueio definitivo. Por isso leia as regras direitinho!",
      },
      {
        q: "Como funciona o presente/gift?",
        a: "Quando o usuário te manda um presente durante a chamada, você ganha moedas extras! Quanto mais caro o presente, mais moedas você recebe.",
      },
      {
        q: "Se não bater a meta, perco as moedas?",
        a: "Não! As moedas ficam guardadas e acumulam pra próxima semana. Nada se perde.",
      },
      {
        q: "Posso divulgar meu Instagram?",
        a: "Não pode! Divulgar redes sociais ou pedir contato fora do app é proibido e pode dar bloqueio.",
      },
      {
        q: "O que é o bloqueio por chamada encerrada?",
        a: "Se o app detectar violação de regras, a chamada é encerrada e você fica bloqueada. 1 chamada = 2h, 2 chamadas = 4h, 3 chamadas = 6h de bloqueio no dia seguinte.",
      },
      { q: "Quero falar com a equipe!", a: "__CTA__" },
    ];

    function toggleChat() {
      document.getElementById("chatBox").classList.toggle("open");
    }

    function renderOptions() {
      const opts = document.getElementById("chatOptions");
      opts.innerHTML = "";
      chatData.forEach((item, i) => {
        const btn = document.createElement("button");
        btn.className = "chat-opt";
        btn.textContent = item.q;
        btn.onclick = () => sendQuestion(i);
        opts.appendChild(btn);
      });
    }

    function sendQuestion(i) {
      const msgs = document.getElementById("chatMessages");
      const userMsg = document.createElement("div");
      userMsg.className = "chat-msg user";
      userMsg.textContent = chatData[i].q;
      msgs.appendChild(userMsg);
      setTimeout(() => {
        const botMsg = document.createElement("div");
        botMsg.className = "chat-msg bot";
        if (chatData[i].a === "__CTA__") {
          botMsg.innerHTML =
            'Claro! 🚀 Fala com a gente no WhatsApp:<br><br><a href="https://wa.me/5521972804151" target="_blank" rel="noopener noreferrer" class="chat-wa-link">Chamar no WhatsApp →</a>';
        } else {
          botMsg.textContent = chatData[i].a;
        }
        msgs.appendChild(botMsg);
        msgs.scrollTop = msgs.scrollHeight;
      }, 600);
      msgs.scrollTop = msgs.scrollHeight;
    }

    renderOptions();