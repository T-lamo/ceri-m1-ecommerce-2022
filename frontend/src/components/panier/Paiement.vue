<script lang="ts" setup>
  import { Form } from "vee-validate";
  import * as Yup from "yup";
  import InputField from "../auth/InputField.vue";
  import { storeToRefs } from "pinia";
  import { useAppStore } from "@/stores";
  import { PaymentDetail } from "@/models";
  import {
    read_lastone_order_detail_byuserid,
    create_payment_detail,
  } from "../../services/crud";
  import Swal from "sweetalert2";

  const {
    list_cart_item,
    current_user,
    total_price,
    current_order_detail,
    current_payement,
  } = storeToRefs(useAppStore());

  /** on invalid submit button */
  const onInvalidSubmit = () => {};
  /** on add paiement */
  const onAddPaiement = async (values: any) => {
    // get last order to get id order to add in payment detail
    let response_read_last_order_byuserid =
      await read_lastone_order_detail_byuserid(current_user.value?.id!);


    //paiement detail
    let my_paiement = new PaymentDetail({
      amount: total_price.value,
      status: "payé",
      created_date: new Date(),
    });
    // add current payment detail
    current_payement.value = my_paiement;
   
    // create paiement details
    Swal.fire({
      title: "Are you sure?",
      text: "You will save payement details",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, pay it!",
    }).then(async (result) => {
      if (result.isConfirmed) {
        Swal.fire(
          "Payed!",
          "Your order of " + total_price.value + " has been paid!",
          "success"
        );
        // create payement detail
        let res = (await create_payment_detail(my_paiement)) as PaymentDetail;


        // update order detail ????
        current_order_detail.value!.payment_status = true;

        // delete list_cart_item
        for (let i = 0; i < list_cart_item.value.length + 1; i++) {
          list_cart_item.value.pop();
        }

      }
    });
  };

  /** generate input validation for Paiement */
  const schema_paiement = Yup.object().shape({
    account_holder: Yup.string().required(),
    provider: Yup.string().required(),
    credit_card_number: Yup.string().required().min(16),
    expiration_date: Yup.string().required(),
    cvv: Yup.number().required().min(3),
  });
</script>

<template>
  <div class="container py-5 my-2">
    <h2 class="text-center">Paiement</h2>
    <div class="card px-3 py-3">
      <div class="row">
        <Form
          @submit="onAddPaiement"
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
            type="password"
            label="CVV/CVC"
            success-message="CVV/CVC name is correct !"
          />
          <div class="text-center pt-1 mb-5 pb-1">
            <button
              class="auth-btn btn btn-outline-warning btn-block"
              type="submit"
            >
              Enregistrer
            </button>
          </div>
        </Form>
      </div>
    </div>
  </div>
</template>
