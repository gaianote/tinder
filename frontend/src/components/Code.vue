<template>
  <el-card class="box-card" shadow="always" style="padding-right: 5px;">
    <div class="clearfix" style="padding-bottom: 10px">
      <span style="padding: 3px 10px 5px 3px; color: #409EFF;">{{
        title
      }}</span>
    </div>
    <div :class="['json-editor', className]">
      <label>
        <textarea ref="textarea"></textarea>
      </label>
    </div>
  </el-card>
</template>

<script>
import CodeMirror from "codemirror";
import "codemirror/addon/lint/lint.css";
import "codemirror/lib/codemirror.css";
import "codemirror/theme/rubyblue.css";

require("script-loader!jsonlint");
import "codemirror/mode/javascript/javascript";
import "codemirror/addon/lint/lint";
import "codemirror/addon/lint/json-lint";

export default {
  name: "jsonEditor",
  data() {
    return {
      jsonEditor: "",
      onlyRead: true,
    };
  },
  props: ["value", "title", "readOnly", "className", "single", "codeValue"],
  watch: {
    value(value) {
      const editor_value = this.jsonEditor.getValue();
      if (value !== editor_value) {
        this.jsonEditor.setValue(JSON.stringify(this.value, null, 2));
        this.jsonEditor.setOption("value", value);
      }
      console.log(value);
    },
  },
  mounted() {
    this.jsonEditor = CodeMirror.fromTextArea(this.$refs.textarea, {
      mode: "application/javascript",
      theme: "default",
      lint: true,
      scrollbarStyle: "null",
      // readOnly: "nocursor",
      height: "auto",
    });
    if (this.readOnly != null) {
      this.onlyRead = this.readOnly;
      this.jsonEditor.setOption("readOnly", this.onlyRead);
      this.jsonEditor.setOption("theme", "xq-dark");
    }

    this.jsonEditor.setValue(JSON.stringify(this.value, null, 2));
    this.jsonEditor.on("change", (cm) => {
      console.log("getValue()", cm.getValue());
      this.$emit("changed", cm.getValue());
      this.$emit("input", cm.getValue());
    });
  },
  methods: {
    getValue() {
      return this.jsonEditor.getValue();
    },
  },
};
</script>

<style>
.json-editor .cm-s-rubyblue span.cm-string {
  color: #f08047;
}

.el-card__header {
  padding: 10px 10px;
}
</style>
