//Tableau Embed function
function initViz() {
    url = "https://public.tableau.com/views/Loans_16029907791890/LoanTerm?:language=en&:display_count=y&:origin=viz_share_link",
    options = {
        hideToolbar: true,
        width: "100%",
        height: "300px",
    };
    viz = new tableau.Viz(tabloananalysis, url, options);
  }

  function initViz() {
    url = "https://public.tableau.com/views/Loans_16029907791890/Dashboard2?:language=en&:display_count=y&:origin=viz_share_link",
    options = {
        hideToolbar: true,
        width: "100%",
        height: "300px",
    };
    viz = new tableau.Viz(tabloananalysis, url, options);
  }