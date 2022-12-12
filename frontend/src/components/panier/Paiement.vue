<script lang="ts" setup>
    import { Form } from 'vee-validate'
    import * as Yup from 'yup'
    import InputField from '../auth/InputField.vue';
    import { useToast } from 'vue-toast-notification';

    /** on invalid submit button */
    const onInvalidSubmit = () => {

    }
    /** on add paiement */
    const onAddPaiement = ((values:any) => {
        
    })

    /** generate input validation for Paiement */
    const schema_paiement = Yup.object().shape({
        account_holder: Yup.string().required(),
        provider: Yup.string().required(),
        credit_card_number: Yup.string().required().min(16),
        expiration_date: Yup.string().required(),
        cvv: Yup.number().required().min(3)
    })

</script>

<template>
    <div class="container py-5 my-2">
        <h2 class="text-center">Paiement</h2>
        <div class="card px-3 py-3">
            <div class="row">
                <Form @submit="onAddPaiement"
                    :validation-schema="schema_paiement"
                    @invalid-submit="onInvalidSubmit"
                    >
                    <InputField
                        name="account_holder"
                        type="text"
                        label="Account holder"
                        placeholder="Jean Jacques GOLDMAN"
                        success-message="Account holder name is correct !"
                        />
                    
                    <InputField
                        name="provider"
                        type="text"
                        label="Provider"
                        placeholder="BNP PARIBAS "
                        success-message="Provider name is correct !"
                        />

                    <InputField
                        name="credit_card_number"
                        type="text"
                        label="Credit card number"
                        placeholder="XXXX XXXX XXXX XXXX "
                        success-message="Credit card name is correct !"
                        />

                    <InputField
                        name="expiration_date"
                        type="text"
                        label="Expiration Date"
                        placeholder="MM/YYYY"
                        success-message="Expiration date is correct !"
                        />
                    <InputField
                        name="cvv"
                        type="number"
                        label="CVV/CVC"
                        success-message="CVV/CVC name is correct !"
                        />
                    <div class="text-center pt-1 mb-5 pb-1">
                        <button class="auth-btn btn btn-outline-warning btn-block" type="submit">
                            Enregistrer
                        </button>
                    </div>
                </Form>    
                <!-- <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Titulaire du compte</p>
                        <input class="form-control mb-3" type="text" placeholder="Name">
                    </div>
                </div> -->

                <!-- <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Nom de la banque </p>
                        <input class="form-control mb-3" type="text" placeholder="Name">
                    </div>
                </div> -->

                <!-- <div class="col-12">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Numero de la carte bancaire</p>
                        <input class="form-control mb-3" type="text" placeholder="0526 8457 996526">
                    </div>
                </div> -->
                
                <!-- <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">Date d'expiration</p>
                        <input class="form-control mb-3" type="text" placeholder="MM/YYYY">
                    </div>
                </div> -->

                <!-- <div class="col-6">
                    <div class="d-flex flex-column">
                        <p class="text mb-1">CVV/CVC</p>
                        <input class="form-control mb-3 pt-2 " type="password" placeholder="***">
                    </div>
                </div> -->

            </div>
        </div>
    </div>
</template>