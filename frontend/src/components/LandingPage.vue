<template>
    <div id="page" class="site">
        <!-- header -->

        <header>
            <!-- header top -->
            <div class="header-top">
                <div class="container">
                    <div class="wrapper flex-item">
                        <div class="left">
                            <ul class="flex-item main-links">
                                <li><a href="#">Blog</a></li>
                                <li><a href="#">Featured Products</a></li>
                                <li><a href="#">Wishing list</a></li>
                            </ul>
                        </div>
                        <div class="right">
                            <ul class="flex-item">
                                <li class="main-links">
                                    <li><a href="#">Sign Up</a></li>
                                    <li><a href="#">My Account</a></li>
                                    <li><a href="#">Order Tracking</a></li>
                                    <li><a href="#">USD<span class="icon-small"></span></a></li>
                                    <li><a href="#">English</a></li>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <!-- header top -->
            <!-- header nav -->
            <div class="header-nav">
                <div class="container">
                    <div class="wrapper flex-item">
                        <a href="#" class="trigger desktop-hide">
                            <span>
                                <font-awesome-icon icon="fa-solid fa-bars" size="lg" :style="{ color: 'black' }"/>
                            </span>
                        </a>
                        <div class="left flex-item">
                                    <div class="logo">
                                        <a href="#">
                                            <span class="circle"></span>
                                            .Store
                                        </a>
                                    </div>
                                    <nav class="mobile-hide">
                                        <ul class="flex-item second-links">
                                            <li><a href="#">home</a></li>
                                            <li><a href="#">Shop</a></li>
                                            <li>
                                                <a href="#">Women
                                                    <div class="icon-small">
                                                        <font-awesome-icon icon="fa-solid fa-chevron-down" size="lg" :style="{ color: 'black' }"/>
                                                    </div>
                                                </a>
                                            </li>
                                            <li><a href="#">Men</a></li>
                                            <li>
                                                <a href="#">Sports
                                                    <div class="fly-item"><span>New!</span></div>
                                                </a>
                                            </li>
                                        </ul>
                                    </nav>
                        </div>
                        <div class="right">
                            <ul class="flex-item second-links">
                                <li class="mobile-hide">
                                    <a href="#">
                                        <div class="icon-large"><font-awesome-icon icon="fa-solid fa-heart" size="lg" :style="{ color: 'red' }"/></div>
                                        <div class="fly-item"><span class="item-number">8</span></div>
                                    </a>
                                </li>
                                <li>
                                    <a href="#" class="iscart">
                                        <div class="icon-large">
                                            <font-awesome-icon icon="fa-solid fa-cart-shopping" size="lg" :style="{ color: 'black' }"/>
                                            <div class="fly-item"><span class="item-number">8</span></div>
                                        </div>
                                        <div class="icon-text">
                                            <div class="mini-text">Total</div>
                                            <div class="cart-total">$0.00</div>
                                        </div>
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <!-- header nav -->
        </header>
        <main></main>
        <!-- footer -->
        <footer></footer>
    </div>
</template>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;600;700&800&family=Rubik:wght@300;400;500&display=swap");
:root {
    --primary-color: #ff6b6b;
    --secondary-color: #2980b9;
    --secondary-dark-color: #7f8c8d;

    --white-color: #ffffff;
    --light-bg-color: #f2f3f5;
    --light-text-color: #7c899a;
    --border-color: #e5e8ec;
    --dark-color: #0a021c;

    --font-small: 13px;
    --font-smaller: 11px;

    --percent100: 13px;
    --percent50: 50%;

    --fw3: 300;
    --fw5: 500;
    --fw6: 600;
    --fw8: 800;

    --trans-background-color: background-color .3s, color .3s;
    --trans-background: background-color .3s;
    --trans-color: color .3s;
}
body {
    font-family: 'Rubik', sans-serif;
    font-size: 16px;
    font-weight: 4380;
    line-height: 1.4;
    color: var(--dark-color);
    background-color: var(--white-color);
}
a {
    text-decoration: none;
    color: inherit;
    /**-webkit-tap-highlight-color: transparent;*/
}
ul {
    list-style: none;
}
img {
    max-width: var(--percent100);
    vertical-align: middle;
}
strong {
    font-weight: var(--fw8);
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}
input::placeholder {
    font: inherit;
}
.container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 0.938em;
}
.column {
    margin-left: -0.935em;
    margin-right: -0.935em;
}
.column .row {
    padding: 0 0.938;
}
.flexwrap {
    display: flex;
    align-items: center;
    justify-content: center;
}
.flex-item {
    display: flex;
    align-items: center;
}
.flexcol{
    display: flex;
    flex-direction: column;
    gap: 1em;
}
.main-links a:hover {
    color: var(--secondary-color);
}
.second-links a:hover {
    color: var(--light-bg-color);
}

/** Headers */
header li > a {
    display: flex;
    position: relative;
    line-height: inherit;
    transition: var(--trans-color);
}
/** header top */
.header-top .wrapper {
    font-size: var(--font-small);
    font-weight: var(--fw3);
    justify-content: space-between;
    line-height: 40px;
}
.header-top .wrapper ul{
    gap: 2em;
}
.header-top li {
    position: relative;
}
.mobile-hide {
    display: none;
}
/** header nav */
.trigger {
    font-size: 1.5em;
    display: flex;
    padding: 0.25em;
    margin-right: 0.5em;
}
.logo a {
    font-family: 'Poppins';
    font-size: 1.75em;
    position: relative;
    font-weight: 800;
    display: flex;
    padding-left: 0.75em;
    margin-right: 2em;
}
.circle {
   position: absolute;
   background-color: var(--light-bg-color);
   top: -15px;
   border-radius: 50%; 
   height: 38px;
   width: 38px;
   left: 0; 
}
.circle::before {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background-color: #2980b9;
    bottom: 5px;
    right: 5px;
    opacity: .4;
    position: absolute;
    content: '';
}
.header-nav nav > ul {
    line-height: 100px;
    gap: 2em;
}
.fly-item {
    position: absolute;
    height: 16px;
    font-weight: 13px;
    padding: 3px;
    text-align: center;
    line-height: 10px;
    color: white;
}
nav .fly-item {
    background-color: #ff6b6b;
    border-radius: 3px;
    top: 50%;
    right: -32px;
    margin-top: -24px;
    width: 30px;
}
.header-nav .right {
    position: relative;
    margin-left: auto;
}
.header-nav .right .icon-large {
    position: relative;
    margin-left: auto;
}
.header-nav .right .fly-item {
    top: 0;
    right: 16px;
    width: 16px;
    background-color: #2980b9;
    border-radius: 50%;
}
/** responsiveness **/
@media screen and (min-width: 992px) {
    .container{
        padding: 0 2em;
    }
    .desktop-hide {
        display: none;
    }
    .mobile-hide{
        display: block;
    }
    .logo a {
        margin-right: 2em;
    }
    .header-nav {
        padding: 0;
        margin: 0;
        border-bottom: 0;
    }
}


</style>