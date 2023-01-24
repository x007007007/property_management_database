<template>
  <div>
    <ul v-if="this.dataChildren">
      < v-for="(item, i) in dataChildren"
                :key="item.id"
                :id="item.id"
                v-model="dataChildren[i]"
                :lazyChildrenLoader="lazyChildrenLoader"
                :addChild="addChild"
                :editable="editable"
      ></TreeItem>
    </ul>
  </div>
</template>
TreeItem
<script>
import TreeItem from "@/components/TreeItem";
export default {
  name: "TreeList",
  components: {TreeItem},
  model: {
    prop: 'value',
    event: 'change'
  },
  props: {
    value: {
      type: Array
    },
    editable: {
      type: Boolean,
      default: false,
    },
    id: null,
    lazyChildrenLoader: {
      type: Function,
    },
    addChild: {
      type: Function,
      default: (val) => {
        console.log(`val:${val}`)
        return !confirm(val)
      }
    }
  },
  data () {
    return {
      dataChildren: this.value || []
    }
  },
  methods: {
    addNode () {

    }
  }
}
</script>

<style scoped>
  div {
    padding: 0;
    margin: 0;
    text-align: left;
  }
  span.root {
    border: solid;
  }
  ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
    border: solid #42b983 1px;
  }
</style>