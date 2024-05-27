const getOptionChart_foot = async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/get_foot");
        return await response.json();
    } catch (ex) {
        console.log("error de red");
    }
};

const initChart = async () => {
    const myChart_foot = echarts.init(document.getElementById("graph_foot"));
    myChart_foot.setOption(await getOptionChart_foot());
};

window.addEventListener("load", async () => {
    await initChart();
    const myChart_foot = echarts.init(document.getElementById("graph_foot"));

    setInterval(async () => {
        await initChart();
    }, 100);

    setInterval(async () => {
        myChart_foot.resize();


    }, 100);

});