<template>
  <div class="hello">
    {{ result }}
    <TreeList
        v-model="result"
        :editable="true"
    ></TreeList>
  </div>
</template>
<script>
import axios from 'axios'
import TreeList from "@/components/TreeList";

export default {
  name: 'HelloWorld',
  components: {TreeList},
  props: {
    msg: String
  },
  data () {
    return {
      result: [
        {
          id: 1,
          name: 'top',
          children: [
            {
              id: 2,
              name: 'lvl2',
              children: [
                {
                  id: 3,
                  name: 'lvl3'
                }
              ]
            }
          ]
        }
      ]
    }
  },
  methods: {
    async updateResourceList() {
      let res = await axios.get("")
      return res
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
