<template>
    <div class="container py-5 my-2">
        <h2 class="text-center">Livraison</h2>
        <div class="accordion" id="accordionExample">
            <!-- A domicile -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    A domicile
                </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong class="text-center">Definir votre adresse: </strong>
                        <div class="col-12">
                            
                            <div class="d-flex flex-column">
                                <p class="text mb-1">Adresse 1</p>
                                <input class="form-control mb-3" type="text" placeholder="154 Bd Premiere Div BLindee">
                            </div>
                            <div class="col-12">
                                <div class="d-flex flex-column">
                                    <p class="text mb-1">Ville</p>
                                    <input class="form-control mb-3" type="text" placeholder="Avignon">
                                </div>
                            </div>

                            <div class="col-12">
                                <div class="d-flex flex-column">
                                    <p class="text mb-1">Boite postale</p>
                                    <input class="form-control mb-3 pt-2 " type="number" placeholder="84000">
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
            <!-- Point de relais -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Au point de relais
                </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong>Choisissez votre point de relais</strong>
                        <div class="col-12">
                            <div class="d-flex flex-column">
                                <p class="text mb-1 mt-4">Ville</p>
                                <input class="form-control mb-3" type="text" placeholder="Avignon">
                            </div>
                        </div>
                        <select class="form-select mb-3" aria-label=".form-select-lg example">
                            <option selected>Choisir le point de relais</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                    </div>
                </div>
            </div>
            <!-- Au depot -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                    A un depot le plus proche de chez vous
                </button>
                </h2>
                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong>Choisissez le depot </strong>
                        <div class="col-12">
                            <div class="d-flex flex-column">
                                <p class="text mb-1 mt-4">Ville</p>
                                <input class="form-control mb-3" type="text" placeholder="Avignon">
                            </div>
                        </div>
                        <select class="form-select mb-3" aria-label=".form-select-lg example">
                            <option selected>Choisir le lieu de depot</option>
                            <option value="1">One</option>
                            <option value="2">Two</option>
                            <option value="3">Three</option>
                        </select>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>