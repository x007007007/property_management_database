<template>
  <li v-show="!draggingChild" ondrop="onDrop">
    <div v-show="!draggingItem">
      <div class="title-widget">
        <button
            draggable="true"
            @drag="onDragItem"
            @dragstart="onDragItemStart"
            @dragend="onDragItemEnd"
        >move</button>
        <button
            draggable="true"
            @drag="onDragSub"
            @dragstart="onDragSubStart"
            v-if="dataChildren.length > 0"
            @click="hiddenChild=!hiddenChild"
        >
          <span v-if="hiddenChild">+</span>
          <span v-else>-</span>
        </button>
        <span class="title">{{ value && value.name }}</span>
        <button v-if="editable && !hiddenChild" @click="creating = true">+</button>
        <button v-if="editable && !hiddenChild" @click="$emit('node-remove', id)">-</button>
      </div>
      <div v-if="creating" class="createWidget">
        <input type="text" v-model="createInput"/>
        <button @click="addItem">v</button>
        <button @click="creating = false">x</button>
      </div>
    </div>
    <transition name="sub-list">
     <ul v-show='!hiddenChild' v-if="dataChildren" class="sub-tree">
        <tree-item v-for="(item, i) in dataChildren"
                   :key="item.id"
                   :id="item.id"
                   v-model="dataChildren[i]"
                   :lazyChildrenLoader="lazyChildrenLoader"
                   :addChild="addChild"
                   :editable="editable"
                   @node-remove="onRemoveNode"
        ></tree-item>
    </ul>
    </transition>
  </li>
</template>

<script>

export default {
  name: "TreeItem",
  model: {
    prop: 'value',
    event: 'input'
  },
  props: {
    id: null,
    value: null,
    editable: {
      type: Boolean,
      default: false,
    },
    name: {
      type: String,
    },
    lazyChildrenLoader: {
      type: Function,
    },
    addChild: {
      type: Function,
    },
    vHiddenChild: {
      type: Boolean,
      default: false
    },
  },
  data () {
    return {
      draggingItem: false,
      draggingChild: false,
      hiddenChild: this.vHiddenChild,
      creating: false,
      createInput: "",
      dataChildren: (this.value && this.value.children && [...this.value.children]) || []
    }
  },
  methods: {
    async addItem () {
      let cb_res = null
      if (this.addChild instanceof Promise) {
        cb_res = await this.addChild(this.createInput)
      } else if (this.addChild instanceof Function) {
        cb_res = this.addChild(this.createInput)
      }
      console.log(cb_res)
      if (!cb_res) {
        this.dataChildren.unshift({
          name: this.createInput,
          id: this.createInput,
          children: []
        })
        this.creating = false
        this.createInput = ''
        this.$emit('input', {...this.value, children: this.dataChildren})
      }
    },
    createFinish () {
      this.creating = false
    },
    removeNode () {
      console.log('')
    },
    onRemoveNode (e) {
      this.dataChildren = this.dataChildren.filter((node) => {
        return e !== node.id
      })
      this.$emit('input', {...this.value, children: this.dataChildren})
    },
    onDragSub (e) {
      this.draggingChild = true
      console.log(e)
    },
    onDragSubStart (e) {
      console.log("onDragSubStart", e)
    },
    onDragItemStart (e) {
      this.draggingItem = true
      console.log("onDragItemStart", e)
    },
    onDragItem (e) {
      console.log(e)
    },
    onDragItemEnd (e) {
      this.draggingItem = false
      console.log(e)
    },
    onDrop (e) {
      console.log(e)
    }
  }
}
</script>

<style scoped>
  .title {
    display: inline-block;
    padding: 0 10px;
    margin: 10px 1px;
    cursor: grab;
    border: dashed 1px;
    user-select: all;
  }
  .createWidget {
    padding: 0 0 0 20px;
  }
  ul {
    list-style-type: none;
    padding: 0 0 0 20px;
    margin: 0;
    border: solid #42b983 1px;
  }
  .sub-list-sub {
    padding: 0px;
  }
  .sub-list-enter-active,
  .sub-list-leave-active {
    transition: all .3s ease;
  }
  .sub-list-enter,
  .sub-list-leave-to
  {
    opacity: 0;
    height: 0px;
  }
</style>