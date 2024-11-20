<template>
  <div>
    <h2>Uploaded Files</h2>
    <div v-if="!files || files.length === 0">
      <p>No files uploaded</p>
    </div>
    <ul v-else>
      <li
        v-for="file in files"
        :key="file.id"
        @click="selectFile(file.id)"
        @mouseover="hoveredFileId = file.id"
        @mouseleave="hoveredFileId = null"
        :class="{'hovered': hoveredFileId === file.id}"
      >
        <strong>{{ file.filename }}</strong> - {{ file.upload_date }} - {{ file.row_count }} rows
        <ul>
          <li v-for="col in file.columns" :key="col.name">
            {{ col.name }} ({{ col.type }})
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: ['files'],
  data() {
    return {
      hoveredFileId: null,
    };
  },
  methods: {
    selectFile(fileId) {
      this.$emit('fileSelected', fileId);
    },
  },
};
</script>

<style scoped>
li {
  cursor: pointer;
  margin-bottom: 10px;
}

li:hover {
  background: #f0f0f0;
}

.hovered {
  background-color: #d0e0f0;
}
</style>
