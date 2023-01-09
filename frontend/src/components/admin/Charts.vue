<script lang="ts" setup>
    import { Chart as ChartJS,Title,Tooltip,Legend,ArcElement,BarElement,CategoryScale,LinearScale } from 'chart.js'
    import { Bar, Pie } from 'vue-chartjs'
    import { read_turnover_per_month } from '@/services/crud';
    import { onMounted } from 'vue';

    onMounted(async () => {
        // let pie = await read_pie_order_details()
        let hist = await read_turnover_per_month(2022)
        // console.log(pie)
        console.log(hist)
    }),
    ChartJS.register(
        CategoryScale,
        LinearScale,
        BarElement,
        ArcElement,
        Title,
        Tooltip,
        Legend
    )

    const data_turnover_per_month = {
    labels: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ],
      datasets: [
        {
            label: 'Turn over per month',
            backgroundColor: '#2980b9',
            data: [40, 20, 12, 39, 10, 40, 39, 20, 40, 20, 12, 11]
        }
      ]
    }

    const data_category_most_bought = {
        labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
        datasets: [
            {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
            data: [40, 20, 80, 10]
            }
        ]
        }

    const options = {
        responsive: true,
        maintainAspectRatio: true
    }


</script>
<template>
    <div class="container-fluid pt-4" >
        <div class="row">
            <!-- TTurn over each year  -->
            <div class="col-md-8 justify-content-start">
                <h5>Turn over per month</h5>
                <Bar
                    :data="data_turnover_per_month"
                    :options="options"
                    />
            </div>
             <!-- Category the most bought -->
             <div class="col-md-4 justify-content-end">
                <h5>Turn over per category</h5>
                <Pie
                    :data="data_category_most_bought"
                    :options="options"
                    />
             </div>
        </div>
        <!-- <div class="row d-flex pt-2">
            <div>
                Une autre graphe
            </div>
        </div> -->
    </div>
    
</template>