function renderGrid() {
  var diyList = document.getElementById("diy-list");
  if (diyList) {
    var blocks = diyList.children;
    var cols = 4, newleft, newtop;
    for(var i = 1; i < blocks.length; i++) {
      if (i % cols == 0) {
        newtop = (blocks[i-cols].offsetTop + blocks[i-cols].offsetHeight);
          blocks[i].style.top = newtop+"px";
      } else {
        if(blocks[i-cols]) {
          newleft = (blocks[i-cols].offsetTop + blocks[i-cols].offsetHeight);
          blocks[i].style.top = newleft+"px";
        }
        newleft = (blocks[i-1].offsetLeft + blocks[i-1].offsetWidth);
        blocks[i].style.left = newleft+"px";  
      }
    }
  }
}
window.addEventListener("load", renderGrid, false);
window.addEventListener("resize", renderGrid, false);