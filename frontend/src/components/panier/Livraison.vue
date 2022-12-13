<script lang="ts" setup>
    import * as Yup from 'yup';
    import { Form } from 'vee-validate';
    import InputField from "../auth/InputField.vue";
    import { useAppStore } from '@/stores';
    import { storeToRefs } from 'pinia';
import { UserAddress } from '@/models';

    const { shipping_chosen , current_user} = storeToRefs(useAppStore())

    /** */
    const onAddAdress = ((values:any) => {
       
        shipping_chosen.value = new UserAddress({
            "adress_line1": values.adress1,
            "adress_line2" : "",
            "city": values.city,
            "country": values.country,
            "created_date": new Date(),
            "mobile": values.phone_number,
            "user_id": current_user.value?.id
        })
        console.log("on add address")
        console.log(shipping_chosen.value)
    })

    const onAddRelaypoint = ((values:any) => {
        shipping_chosen.value = new UserAddress({
            "adress_line1": values.adress_relay_point,
            "adress_line2" : "",
            "city": values.city,
            "country": values.country,
            "created_date": new Date(),
            "mobile": values.phone_number,
            "user_id": current_user.value?.id
        })
        console.log("on add relay point adress")
        console.log(shipping_chosen.value)
    })
    const onAddDeposit = ((values:any) => {
        shipping_chosen.value = new UserAddress({
            "adress_line1": values.adress_deposit,
            "adress_line2" : "",
            "city": values.city,
            "country": values.country,
            "created_date": new Date(),
            "mobile": values.phone_number,
            "user_id": current_user.value?.id
        })
        console.log("on add deposit address")
        console.log(shipping_chosen.value)
    })

    /** on invalid submit */
    const onInvalidSubmit = (()=> {
      console.log('invalid button me')
      const submitBtn = document.querySelector('.auth-btn');
      submitBtn!.classList.add('invalid');
      setTimeout(() => {
        submitBtn!.classList.remove('invalid');
      }, 1000);
    })

    /** generate input validation for Home section */
    const schema_home = Yup.object().shape({
        country: Yup.string().required(),
        adress1: Yup.string().required(),
        city: Yup.string().required(),
        postal_code: Yup.number().required().min(5),
        phone_number: Yup.number().min(9)

    })

    /** generate input validation for relay point */
    const schema_relaypoint = Yup.object().shape({
        country: Yup.string().required(),
        city: Yup.string().required(),
        postal_code: Yup.number().required().min(5),
        adress_relay_point: Yup.string().required(),
        phone_number: Yup.number().min(9)
    })

    /**  generate input validation for deposit office */
    const schema_deposit = Yup.object().shape({
        country: Yup.string().required(),
        city: Yup.string().required(),
        adress_deposit: Yup.string().required(),
        postal_code: Yup.number().required(),
        phone_number: Yup.number().min(9)
    })
</script>

<template>
    <div class="container py-5 my-2">
        <h2 class="text-center">Livraison</h2>
        <div class="accordion" id="accordionExample">
            <!-- A domicile -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    Home
                </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong class="text-center">Define your adress: </strong>
                        <div class="col-12">
                            <Form @submit="onAddAdress"
                                :validation-schema="schema_home"
                                @invalid-submit="onInvalidSubmit"
                                >
                                <InputField
                                    name="country"
                                    type="text"
                                    label="Country"
                                    placeholder="Your country"
                                    success-message="Country name is correct !"
                                    />

                                <InputField
                                    name="city"
                                    type="text"
                                    label="City"
                                    placeholder="Your address"
                                    success-message="City name is correct !"
                                    />
                               
                                <InputField
                                    name="postal_code"
                                    type="text"
                                    label="Postal code"
                                    placeholder="84000"
                                    success-message="Postal code is correct !"
                                    />

                                <InputField
                                    name="adress1"
                                    type="text"
                                    label="Adress 1"
                                    placeholder="Your address"
                                    success-message="Address is correct !"
                                    />

                                <InputField
                                    name="phone_number"
                                    type="text"
                                    label="Phone number"
                                    placeholder="856325699"
                                    success-message="Phone number is correct !"
                                    />
                                <div class="text-center pt-1 mb-5 pb-1">
                                    <button class="auth-btn btn btn-outline-warning btn-block" type="submit">
                                        Enregistrer
                                    </button>
                                </div>
                            </Form>

                        </div>
                    </div>
                </div>
            </div>
            <!-- Point de relais -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingTwo">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    Relay point
                </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong>Choose your relay point </strong>
                        <div class="col-12">
                            <Form @submit="onAddRelaypoint"
                                :validation-schema="schema_relaypoint"
                                @invalid-submit="onInvalidSubmit"
                                >
                                <InputField
                                    name="country"
                                    type="text"
                                    label="Country"
                                    placeholder="Your country"
                                    success-message="Country name is correct !"
                                    />

                                <InputField
                                    name="city"
                                    type="text"
                                    label="City"
                                    placeholder="City name"
                                    success-message="City is correct !"
                                    />
                                <InputField
                                    name="postal_code"
                                    type="text"
                                    label="Postal code"
                                    placeholder="84000"
                                    success-message="Postal code is correct !"
                                    />
                                <InputField
                                    name="adress_relay_point"
                                    type="text"
                                    label="Adress of relay point"
                                    placeholder="52 rue ciboulette "
                                    success-message="Email address correct !"
                                    />
                                <InputField
                                    name="phone_number"
                                    type="text"
                                    label="Phone number"
                                    placeholder="856325699"
                                    success-message="Phone number is correct !"
                                    />
                            </Form>
                            <div class="text-center pt-1 mb-5 pb-1">
                                <button class="auth-btn btn btn-outline-warning btn-block" type="submit">
                                    Enregistrer
                                </button>
                            </div>
                        </div>
                        
                    </div>
                   
                </div>
            </div>
            <!-- Au depot -->
            <div class="accordion-item">
                <h2 class="accordion-header" id="headingThree">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                    Nearest deposit office
                </button>
                </h2>
                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample">
                    <div class="accordion-body">
                        <strong>Choose a deposit office</strong>
                        <Form @submit="onAddDeposit"
                                :validation-schema="schema_deposit"
                                @invalid-submit="onInvalidSubmit"
                                >
                            <InputField
                                name="country"
                                type="text"
                                label="Country"
                                placeholder="Your country"
                                success-message="Country name is correct !"
                                />
                            <InputField
                                name="adress_deposit"
                                type="text"
                                label="Adresse"
                                placeholder="6 rue de la palais "
                                success-message="Adress is correct !"
                                />
                            <InputField
                                name="city"
                                type="text"
                                label="City"
                                placeholder="Avignon "
                                success-message="City is correct !"
                                />
                            <InputField
                                name="postal_code"
                                type="number"
                                label="Postal code"
                                success-message="Postal code is correct !"
                                />
                            <InputField
                                name="phone_number"
                                type="text"
                                label="Phone number"
                                placeholder="856325699"
                                success-message="Phone number is correct !"
                                />
                            <div class="text-center pt-1 mb-5 pb-1">
                                <button class="auth-btn btn btn-outline-warning btn-block" type="submit">
                                    Enregistrer
                                </button>
                            </div>
                        </Form>
                           
                        <!-- <div class="col-12">
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

                        <div class="col-12">
                            <div class="d-flex flex-column">
                                <p class="text mb-1">Phone number</p>
                                <input class="form-control mb-3 pt-2 " type="number" placeholder="652869574" min="0">
                            </div>
                        </div> -->
                    </div>

                   
                </div>
            </div>
        </div>
    </div>
    
</template>