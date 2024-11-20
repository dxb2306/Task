<template>
    <div>
      <h2>Upload a File</h2>
      <input type="file" @change="uploadFile" />
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      async uploadFile(event) {
        const file = event.target.files[0];
        if (!file) return;
  
        const formData = new FormData();
        formData.append('file', file);
  
        const response = await fetch('http://localhost:8080/api/upload', {
          method: 'POST',
          body: formData,
        });
  
        if (response.ok) {
          this.$emit('fileUploaded');
        } else {
          alert('File upload failed.');
        }
      },
    },
  };
  </script>
  
  <style>
  div {
    margin-bottom: 20px;
  }
  </style>
  