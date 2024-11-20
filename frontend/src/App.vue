<template>
  <div id="app">
    <h1>File Manager</h1>
    <FileUpload @fileUploaded="fetchFiles" />
    <FileList :files="files" @fileSelected="fetchFileContent" />
    <FileContent v-if="selectedFileContent" :content="selectedFileContent" />
  </div>
</template>

<script>
import FileUpload from './components/FileUpload.vue';
import FileList from './components/FileList.vue';
import FileContent from './components/FileContent.vue';

export default {
  components: { FileUpload, FileList, FileContent },
  data() {
    return {
      files: [],
      selectedFileContent: null,
    };
  },
  methods: {
    async fetchFiles() {
      const response = await fetch('http://localhost:8080/api/files');
      this.files = await response.json();
    },
    async fetchFileContent(fileId) {
      const response = await fetch(`http://localhost:8080/api/file/${fileId}`);
      this.selectedFileContent = await response.json();
    },
  },
  created() {
    this.fetchFiles();
  },
};
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  max-width: 800px;
  margin: auto;
  padding: 20px;
}
</style>
