document.addEventListener('DOMContentLoaded', () => {

    // --- CURSOR ENGINE ---
    const cursorDot = document.getElementById('cursor-dot');
    const cursorOutline = document.getElementById('cursor-outline');
    const interactiveElements = document.querySelectorAll('a, button, .sidebar-nav .nav-item, .faq-widget');

    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;

        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: 'forwards' });
    });

    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
        el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
    });

    // --- SPOTLIGHT EFFECT ---
    const spotlight = document.getElementById('spotlight');
    window.addEventListener('mousemove', (e) => {
        spotlight.style.background = `radial-gradient(circle at ${e.clientX}px ${e.clientY}px, rgba(173, 0, 255, 0.15), transparent 30%)`;
    });

    // --- LETTER-BY-LETTER FORMING EFFECT (for titles and bios) ---
    const formingText = (element) => {
        const originalText = element.textContent;
        element.textContent = ''; // Limpa o texto original
        let index = 0;
        const interval = setInterval(() => {
            if (index < originalText.length) {
                element.textContent += originalText[index];
                index++;
            } else {
                clearInterval(interval);
            }
        }, 100); 
    };

    // --- TYPING EFFECT (for FAQ content) ---
    const typingEffect = (element, text, speed) => {
        element.innerHTML = '';
        let i = 0;
        const typeInterval = setInterval(() => {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                element.scrollTop = element.scrollHeight; // Auto-scroll
            } else {
                clearInterval(typeInterval);
            }
        }, speed);
    };

    // --- BIOS PRELOADER & INITIATION ---
    const preloader = document.getElementById('preloader');
    const biosTextEl = document.getElementById('bios-text');
    let bootSequenceTimeout;

    const biosLines = [
        "<span>WBC_BIOS v3.0 PRIME INTERFACE</span>",
        "<span>(c) 2024 WESLEY BOTCRAFT. All Rights Reserved.</span>",
        "<span></span>",
        "<span>Initializing Kinetic UI Engine... <span class='success'>OK</span></span>",
        "<span>Calibrating Reactive Spotlight... <span class='success'>OK</span></span>",
        "<span>Loading Data Core... <span class='success'>OK</span></span>",
        "<span>Verifying DOM Integrity... <span class='success'>OK</span></span>",
        "<span></span>",
        "<span class='success'>All systems nominal. Engaging user interface.</span>"
    ];

    const startBootSequence = () => {
        let i = 0;
        const typeLine = () => {
            if (i < biosLines.length) {
                biosTextEl.innerHTML += biosLines[i] + "\n";
                biosTextEl.scrollTop = biosTextEl.scrollHeight;
                i++;
                bootSequenceTimeout = setTimeout(typeLine, Math.random() * 150 + 50);
            } else {
                setTimeout(hidePreloader, 500);
            }
        };
        typeLine();
    };

    const hidePreloader = () => {
        clearTimeout(bootSequenceTimeout);
        preloader.style.opacity = '0';
        preloader.style.visibility = 'hidden';
        setTimeout(() => {
            document.querySelector('.main-header').style.opacity = '1';
            const scrambleElements = document.querySelectorAll('[data-text-scramble]');
            scrambleElements.forEach(el => {
                const text = el.getAttribute('data-text-scramble');
                el.textContent = text;
                formingText(el);
            });
        }, 200);
    };

    window.addEventListener('keydown', hidePreloader, { once: true });
    window.addEventListener('click', hidePreloader, { once: true });
    startBootSequence();

    // --- TAB NAVIGATION SYSTEM ---
    const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    const modules = document.querySelectorAll('.dashboard-module');

    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = item.getAttribute('href');

            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            modules.forEach(module => {
                module.classList.remove('active-module');
                if (module.id === targetId.substring(1)) {
                    setTimeout(() => {
                        module.classList.add('active-module');
                    }, 500);
                }
            });
        });
    });

    // --- FAQ WIDGETS LOGIC ---
    const faqWidgets = document.querySelectorAll('.faq-widget');
    const faqContentArea = document.getElementById('faq-content');

    const faqData = {
        'sobre': "Wesley Botcraft é a sua solução para websites inteligentes e simples. Nossa missão é transformar a experiência online de pequenas empresas e autônomos com a fusão de design intuitivo e funcionalidade conversacional. Oferecemos serviços de criação de interfaces interativas e implementação de sistemas conversacionais programados.",
        'info': "Aqui estão algumas informações úteis e curiosidades:\n\n- Curiosidades do mundo de interfaces com chatbot:\n1. A maioria dos usuários prefere interagir com um chatbot que tenha uma persona clara.\n2. Chatbots podem aumentar as taxas de conversão em até 40%.\n3. A primeira 'chatbot' foi o ELIZA, criado em 1966.\n\n- Benefícios de uma interface com chatbot programado:\n1. Atendimento 24/7 sem a necessidade de um humano.\n2. Qualificação de leads de forma automatizada.\n3. Redução de custos e aumento da eficiência operacional.\n\n- Hospedagem:\nOfereço a opção de hospedagem gratuita com o GitHub Pages para projetos simples, ou a opção de hospedagem paga com domínio próprio para um visual mais profissional e completo.",
        'desenvolvedor': "O criador e arquiteto desta interface é Wesley Santos. Ele se dedica à criação de interfaces digitais minimalistas e funcionais, focadas na experiência do usuário. Seu trabalho visa ajudar pequenas empresas e profissionais autônomos a se destacarem no mercado digital através de soluções de front-end personalizadas e intuitivas.",
        'contato': `
            <p>Pronto para construir o futuro do seu projeto? A comunicação está a um clique de distância.</p>
            <div class="contact-buttons">
                <a href="https://wa.me/5515997920703" target="_blank">
                    <i class="fab fa-whatsapp"></i>
                    <span>WHATSAPP</span>
                </a>
                <a href="https://www.instagram.com/siigmachat" target="_blank">
                    <i class="fab fa-instagram"></i>
                    <span>INSTAGRAM</span>
                </a>
                <a href="mailto:wmktgeo@gmail.com">
                    <i class="fa-solid fa-envelope"></i>
                    <span>E-MAIL</span>
                </a>
            </div>
        `
    };

    faqWidgets.forEach(widget => {
        widget.addEventListener('click', () => {
            const faqId = widget.dataset.faqId;
            const content = faqData[faqId];
            if (content) {
                if (faqId === 'contato') {
                    // Para o conteúdo HTML, apenas injeta e não usa o efeito de digitação
                    faqContentArea.innerHTML = content;
                } else {
                    // Para o texto, usa o efeito de digitação
                    typingEffect(faqContentArea, content, 15);
                }
            }
        });
    });
});