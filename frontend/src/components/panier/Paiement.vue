<template>
    <div class="container py-5 my-2">
        <h2 class="text-center">Paiement</h2>
        <div class="card px-3 py-3">
            <div class="row">
                <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Titulaire du compte</p>
                        <input class="form-control mb-3" type="text" placeholder="Name">
                    </div>
                </div>

                <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Nom de la banque </p>
                        <input class="form-control mb-3" type="text" placeholder="Name">
                    </div>
                </div>

                <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Numero de la carte bancaire</p>
                        <input class="form-control mb-3" type="text" placeholder="0526 8457 996526">
                    </div>
                </div>
                
                <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Date d'expiration</p>
                        <input class="form-control mb-3" type="text" placeholder="MM/YYYY">
                    </div>
                </div>

                <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">CVV/CVC</p>
                        <input class="form-control mb-3 pt-2 " type="password" placeholder="***">
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>