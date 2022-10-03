<template>
    <div class="row-center">
        <div class="wrap">
            <div class="row row-1">
                <div class="card card-1">test</div>
                <div class="row card-1">
                    <div class="card">test</div>
                    <div class="card">test</div>
                    <div class="card">test</div>
                </div>
            </div>
            <div class="row row-2">
                
            </div>
        </div>
    </div>
</template>

<script>
export default {
}
</script>

<style scoped>

.row{
    display:flex;
    gap:24px;
    /* margin-top:40px; */
}
.row-1{
    height:196px;
}
.row-2{
    margin-top:40px;
    height: 562px;
}
.card-1{
    width:50%;
}
</style>