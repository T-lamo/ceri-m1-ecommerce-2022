
const { read_turnover_per_month } from "@/models";
// turn over per month
export const data_turnover_per_month = {
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

// percentage of most bought category
export const data_category_most_bought = {
  labels: ['VueJs', 'EmberJs', 'ReactJs', 'AngularJs'],
  datasets: [
    {
      backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
      data: [40, 20, 80, 10]
    }
  ]
}

export const options = {
    responsive: true,
    maintainAspectRatio: true
  }
  