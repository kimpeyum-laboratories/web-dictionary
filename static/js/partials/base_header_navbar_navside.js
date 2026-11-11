(function() {
    const navbarMenuButton = document.getElementById("navbar-menu-button");
    const navside = document.getElementById("navbar-menu");
    const navsideCloseButton = document.getElementById("navside-close-button");
    
    const toggleNavbarMenu = () => navside?.classList.toggle('is-open');

    navbarMenuButton?.addEventListener('click', toggleNavbarMenu);
    navsideCloseButton?.addEventListener('click', toggleNavbarMenu);
})();
