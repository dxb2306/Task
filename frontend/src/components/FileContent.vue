<template>
    <div>
      <h2>File Content</h2>
      <table border="1">
        <thead>
          <tr>
            <th v-for="header in content.headers" :key="header">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in content.rows" :key="row">
            <td v-for="cell in row" :key="cell">{{ cell }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: ['content'],
  };
  </script>
  
  <style>
  table {
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 8px;
    text-align: left;
  }
  </style>
  