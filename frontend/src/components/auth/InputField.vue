<script setup lang="ts">
    import { defineProps, computed} from 'vue';
    import { useField } from 'vee-validate'

    const props = defineProps ({
        label: {
            type: String,
            required: true,
        },
        name: {
            type: String,
            required: true,
        },
        value: {
            type: String,
        },
        type: {
            type: String,
             default: 'text',
        },
        successMessage: {
            type: String,
            default: '',
        },
        placeholder: {
            type: String,
            default: '',
        }
    })
   
    // const my_name = toRef(props, 'name') or
    const name = computed(() => props.name)

    const {
        value: inputValue,
        errorMessage,
        handleBlur,
        handleChange,
        meta,
    } = useField(name, undefined, {
        initialValue: props.value,
    });

</script>
<template>
<div class="form-floating mb-3 py-2">
    <input
      :name="name"
      :id="name"
      :type="type"
      :value="inputValue"
      :placeholder="placeholder"
      @input="handleChange"
      @blur="handleBlur"
      class="form-control"
      :class="{'is-invalid':!!errorMessage, 'is-valid':meta.valid}"
    />
    <label :for="name">{{ label }}</label>

        <div class="valid-feedback">
            Looks good! {{ successMessage}}
        </div>
        <div class="invalid-feedback">
            Looks bad! {{ errorMessage}}
        </div>
</div>
</template>
