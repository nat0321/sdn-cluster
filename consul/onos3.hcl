service {
  name = "onos3"
  id = "onos3"
  address = "175.24.1.7"
  port = 6653

  tags      = ["v1"]
  meta      = {
    version = "1"
  }
  
  connect { 
    sidecar_service {
      port = 20000
      
      check {
        name = "Connect Envoy Sidecar"
        tcp = "175.24.1.7:20000"
        interval ="10s"
      }
    }  
  }
}
