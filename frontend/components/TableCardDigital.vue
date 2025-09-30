<template>
  <div class="card bg-base-100 shadow-xl">
    <div class="card-body">
      <h2 class="card-title">{{ props.name }}</h2>
      <Line 
        :options="{
          maintainAspectRatio: true
        }"
        :data="{
          labels: labelsForHtml,
          datasets: [
            {
              label: 'Veces que se activó en el día',
              backgroundColor: '#2980b9',
              borderColor: '#2980b9',
              data
            }
          ]
        }" />
      <div>
        <div class="collapse bg-base-200">
          <input type="checkbox" />
          <div class="collapse-title font-medium">Tabla de registros</div>
          <div class="collapse-content">
            <div class="overflow-x-auto overflow-y-auto max-h-[20rem]">
              <table class="table">
                <thead>
                  <tr>
                    <th></th>
                    <th>Acción</th>
                    <th>Hora</th>
                    <th>Fecha</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(td, i) in props.tableData">
                    <th>{{ i + 1 }}</th>
                    <td>{{ td.action }}</td>
                    <td>{{ td.time }}</td>
                    <td>{{ td.date }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

const props = defineProps<{
  name: string,
  myId: string,
  tableData: {
    action: string,
    time: string,
    date: string
  }[]
}>();

const countsByDate = computed(() => {
  const filteredData = props.tableData.filter((item) => item.action === 'Encender');

  return filteredData.reduce((acc: any, item) => {
    acc[item.date] = (acc[item.date] || 0) + 1;
    return acc;
  }, {});
})

const labelsForHtml = computed(() => labels.value.map((elem) => elem.substring(0, 5)));
const labels = computed(() => Object.keys(countsByDate.value).sort((a: any, b: any) => new Date(a) - new Date(b)));
const data = computed(() => labels.value.map((label) => countsByDate.value[label]));

</script>