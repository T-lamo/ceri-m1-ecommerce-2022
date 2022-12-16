<script lang="ts" setup>
    import { Form } from 'vee-validate'
    import * as Yup from 'yup'
    import InputField from '../auth/InputField.vue';
    import { useToast } from 'vue-toast-notification';
    import { storeToRefs } from 'pinia';
    import { useAppStore } from '@/stores';
    import { CartItem, OrderDetail, PaymentDetail } from '@/models';
    import { create_order_detail, read_lastone_order_detail_byuserid, create_payment_detail, toast_function } from '../../services/crud'
    import Swal from 'sweetalert2';
    

    const { list_cart_item, current_user, total_price }  = storeToRefs(useAppStore())

    /** on invalid submit button */
    const onInvalidSubmit = () => {

    }
    /** on add paiement */
    const onAddPaiement = (async (values:any) => {
        //shopping session

        // create an order
        let response_create_order = await create_order_detail({
            "user_id": current_user.value?.id!,
            "created_date": new Date(),
            "total": total_price.value,
        })

        // get last order to get id order to add in payment detail
        let response_read_last_order_byuserid = await read_lastone_order_detail_byuserid(current_user.value?.id!)

        console.log(response_read_last_order_byuserid)

        //paiement detail
        let my_paiement = new PaymentDetail({
            "amount": total_price.value,
            "created_date": new Date(),
            "credit_card_number": values.credit_card_number ,
            "cvv": values.cvv,
            "expiration_date": values.expiration_date ,
            "name": values.account_holder,
            "order_detail_id": response_read_last_order_byuserid.id,
            "provider": values.provider ,
            "status": "done"
            })
        
        // create paiement details

        let res_payment = await create_payment_detail(my_paiement)
                            .then(res => toast_function("Payment successfully done","success"))
                            .catch(error => toast_function("Error","error"))
                            
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