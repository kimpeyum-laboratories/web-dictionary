document.addEventListener('DOMContentLoaded', () => {
    initClickRouter();
});

function initClickRouter() {
    const navside = document.getElementById('navigation');

    const toggleNav = () => {
        if (navside) navside.classList.toggle('visible');
    };

    const actionMap = {
        'openNavside': toggleNav,
        'closeNavside': toggleNav
    };

    document.addEventListener('click', (event) => {
        const actionElement = event.target.closest('[data-action]');
        if (!actionElement) return;

        const actionName = actionElement.dataset.action;
        
        if (actionMap[actionName]) {
            actionMap[actionName](actionElement, event);
        }
    });
}