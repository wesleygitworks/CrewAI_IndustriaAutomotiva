document.addEventListener("DOMContentLoaded", () => {
    
    // --- PRELOADER ---
    const preloader = document.getElementById('preloader');
    window.addEventListener('load', () => {
        preloader.classList.add('loaded');
    });

    // --- CURSOR PERSONALIZADO ---
    const cursor = document.querySelector('.custom-cursor');
    document.addEventListener('mousemove', e => {
        cursor.setAttribute("style", "top: "+(e.pageY - 10)+"px; left: "+(e.pageX - 10)+"px;")
    });
    
    document.addEventListener('click', () => {
        cursor.classList.add("expand");
        setTimeout(() => {
            cursor.classList.remove("expand");
        }, 500);
    });

    // --- EFEITO DE DIGITAÇÃO NO TÍTULO ---
    const titleText = "WESLEY BOTCRAFT";
    const titleElement = document.querySelector('.main-title');
    let i = 0;
    function typeWriter() {
        if (i < titleText.length) {
            titleElement.innerHTML += titleText.charAt(i);
            i++;
            setTimeout(typeWriter, 150);
        }
    }
    typeWriter();

    // --- NAVEGAÇÃO MÓVEL (HAMBURGER) ---
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });
    
    // Fechar menu ao clicar em um link
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // --- ACORDEÃO FAQ ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        const answer = item.querySelector('.faq-answer');
        
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Fecha todos os outros itens
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                otherItem.querySelector('.faq-answer').style.maxHeight = 0;
            });
            
            // Abre ou fecha o item clicado
            if (!isActive) {
                item.classList.add('active');
                answer.style.maxHeight = answer.scrollHeight + "px";
            }
        });
    });
    
    // --- ANIMAÇÃO DE SCROLL NAS SEÇÕES ---
    const sections = document.querySelectorAll('.content-section');
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });
    
    // --- ATIVAR LINK DE NAVEGAÇÃO NO SCROLL ---
    const navLinks = document.querySelectorAll('.nav-link');
    const contentSections = document.querySelectorAll('main section');

    const activateNavLink = () => {
        let currentSection = '';
        contentSections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 70) { // 70 é a altura do header
                currentSection = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href').substring(1) === currentSection) {
                link.classList.add('active');
            }
        });
    };
    
    window.addEventListener('scroll', activateNavLink);

});