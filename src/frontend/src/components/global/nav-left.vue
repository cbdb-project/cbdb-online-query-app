<template>
  <b-nav vertical class="nav-left">
    <b-nav-item exact to="/index" exact-active-class="active">
      {{ $t("navbarLeft.home") }}
    </b-nav-item>

    <!--实体查询-->
    <b-nav-item>
      <b-button
        v-b-toggle.collapse-a
        variant="link"
        class="text-decoration-none"
        v-on:click="toggleIcon(1)"
      >
        <!--text-decoration-none -> bootstrap 4.3  -->
        <span class="collapse-head-text">{{
          $t("navbarLeft.entityQuery")
        }}</span>
      </b-button>
      <svg
        v-bind:class="{ rotate: icon.isRotate1 }"
        t="1575729721049"
        class="svg-icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="2110"
        width="200"
        height="200"
      >
        <path
          d="M334.4384 127.8976c-5.2224 0-10.5472 1.9456-14.4384 5.9392-7.9872 7.9872-7.9872 20.992 0 28.9792l334.6432 334.6432c7.9872 7.9872 7.9872 20.992 0 28.9792L319.8976 861.184c-7.9872 7.9872-7.9872 20.992 0 28.9792 3.9936 3.9936 9.216 5.9392 14.4384 5.9392s10.5472-1.9456 14.4384-5.9392l349.184-349.184c15.9744-15.9744 15.9744-41.8816 0-57.9584l-349.184-349.184c-3.8912-3.8912-9.1136-5.9392-14.336-5.9392z"
          p-id="2111"
        ></path>
      </svg>
    </b-nav-item>
    <b-collapse id="collapse-a" class="mb-2" :visible="true">
      <b-nav-item
        exact
        to="/q-entity/by-person"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.entityQueryByPersonIntro')"
      >
        {{ $t("navbarLeft.entityQueryByPerson") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-entity/by-entry"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.entityQueryByEntryIntro')"
      >
        {{ $t("navbarLeft.entityQueryByEntry") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-entity/by-office"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.entityQueryByOfficeIntro')"
      >
        {{ $t("navbarLeft.entityQueryByOffice") }}
      </b-nav-item>
    </b-collapse>

    <!--关系查询-->
    <b-nav-item>
      <b-button
        v-b-toggle.collapse-b
        variant="link"
        class="text-decoration-none"
        v-on:click="toggleIcon(2)"
      >
        <!--text-decoration-none -> bootstrap 4.3  -->
        <span class="collapse-head-text">{{
          $t("navbarLeft.relationQuery")
        }}</span>
      </b-button>
      <svg
        v-bind:class="{ rotate: icon.isRotate2 }"
        t="1575729721049"
        class="svg-icon"
        viewBox="0 0 1024 1024"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        p-id="2110"
        width="200"
        height="200"
      >
        <path
          d="M334.4384 127.8976c-5.2224 0-10.5472 1.9456-14.4384 5.9392-7.9872 7.9872-7.9872 20.992 0 28.9792l334.6432 334.6432c7.9872 7.9872 7.9872 20.992 0 28.9792L319.8976 861.184c-7.9872 7.9872-7.9872 20.992 0 28.9792 3.9936 3.9936 9.216 5.9392 14.4384 5.9392s10.5472-1.9456 14.4384-5.9392l349.184-349.184c15.9744-15.9744 15.9744-41.8816 0-57.9584l-349.184-349.184c-3.8912-3.8912-9.1136-5.9392-14.336-5.9392z"
          p-id="2111"
        ></path>
      </svg>
    </b-nav-item>
    <b-collapse id="collapse-b" class="mb-2" :visible="true">
      <b-nav-item
        exact
        to="/q-relation/by-place"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.entityQueryByPlace')"
      >
        {{ $t("navbarLeft.entityQueryByPlace") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-relation/two-person"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.relationQueryTwoPerson')"
        disabled
      >
        {{ $t("navbarLeft.relationQueryTwoPerson") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-relation/kinship"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.relationQueryByKinship')"
      >
        {{ $t("navbarLeft.relationQueryByKinship") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-relation/association"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.relationQueryByAssociation')"
      >
        {{ $t("navbarLeft.relationQueryByAssociation") }}
      </b-nav-item>
      <b-nav-item
        exact
        to="/q-relation/by-social-network"
        exact-active-class="active"
        v-b-tooltip.hover.right
        :title="$t('navbarLeft.relationQueryBySocialNetwork')"
        disabled
      >
        {{ $t("navbarLeft.relationQueryBySocialNetwork") }}
      </b-nav-item>
    </b-collapse>
  </b-nav>
</template>

<script>
export default {
  name: "navbarLeft",
  data() {
    return {
      icon: {
        //isRotate[n] V型按钮的旋转状态，是否顺时针转90度。当控制折叠的按钮被点选时 isRotate 的值会 toogle
        isRotate1: true,
        isRotate2: true,
        isRotate3: true
      }
    };
  },
  methods: {
    //toogleIcon 操作V型按钮的旋转
    toggleIcon: function(idx) {
      if (idx == 1) this.icon.isRotate1 = !this.icon.isRotate1;
      else if (idx == 2) this.icon.isRotate2 = !this.icon.isRotate2;
      else if (idx == 3) this.icon.isRotate3 = !this.icon.isRotate3;
    }
  }
};
</script>
<style scoped>
.svg-icon {
  padding: 0;
  margin-left: -0.4em;
  width: 1em;
  height: 1em;
  transition: all 0.4s;
}
.rotate {
  transform: rotate(90deg);
  transition: all 0.4s;
}
.collapse-head-text {
  color: #4d4d4d;
}
.active {
  background-color: #409eff;
  color: #ffffff;
}
.nav-left {
  width: auto;
}
.nav-item {
  min-width: 150px;
}
</style>
