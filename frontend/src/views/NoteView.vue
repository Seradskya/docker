<template>
  <div v-if="note">
    <p><strong>Title:</strong> {{ note.title }}</p>
    <p><strong>Content:</strong> {{ note.content }}</p>

    <div>
      <p><router-link :to="{name: 'EditNote', params:{id: note.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeNote()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'MyNote',
  props: ['id'],
  async created() {
    try {
      await this.viewNote(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/');
    }
  },
  computed: {
    ...mapGetters({ note: 'stateNote', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewNote', 'deleteNote']),
    async removeNote() {
      try {
        await this.deleteNote(this.id);
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
