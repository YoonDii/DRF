//host,port키보드이벤트
$(document).ready(function(){
  var host = document.getElementById("host");
  var port = document.getElementById("port");
  var helperHost = document.getElementById("helperHost");
  var helperPort = document.getElementById("helperPort");
  var regHost = /^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/;
  var regPort = /^([0-9][0-9][0-9][0-9])$/;

  //host red
  host.addEventListener("change", function(num){
    console.log('change:'+ host.value)
    if(!regHost.test(host.value)){
    host.style.color = "red";
    helperHost.style.display = "inline";
    host.focus();
  }else{
    helperHost.style.display = "none";
  };
  return false;
  });

  //유효성이 통과시 글자색 변경
  host.addEventListener("keyup", Key1, false);
  function Key1(e){
    if (regHost.test(host.value)){
      host.style.color = "black";
      helperHost.style.display = "none";
  };
  return false;
  };

  //port red
  port.addEventListener("change", function(num){
    if(!regPort.test(port.value)){
      port.style.color = "red";
      helperPort.style.display = "inline";
      port.focus();
    }else{
      helperPort.style.display = "none";
  };
  return false;
  });

  //유효성이 통과시 글자색 변경
  port.addEventListener("keyup", Key2, false);
  function Key2(e){
    if (regPort.test(port.value)){
      port.style.color = "black";
      helperPort.style.display = "none";
  };
  return false;
  };
});