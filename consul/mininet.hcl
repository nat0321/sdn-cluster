service {
  name = "mininet"
  id = "mininet"
  address = "175.24.1.9"
  port = 6653
  
  connect { 
    sidecar_service {
      port = 20000
      
      check {
        name = "Connect Envoy Sidecar"
        tcp = "175.24.1.9:20000"
        interval ="10s"
      }

      proxy {
        upstreams {
          destination_name = "onos1"
          local_bind_address = "127.0.0.1"
          local_bind_port = 6001
          config {
            connect_timeout_ms = 5000
            limits {
              max_connections         = 3
              max_pending_requests    = 4
              max_concurrent_requests = 5
            }
            passive_health_check {
              interval     = "30s"
              max_failures = 10
            }
          }
        }
        upstreams {
          destination_name = "onos2"
          local_bind_address = "127.0.0.1"
          local_bind_port = 6002
          config {
            connect_timeout_ms = 5000
            limits {
              max_connections         = 3
              max_pending_requests    = 4
              max_concurrent_requests = 5
            }
            passive_health_check {
              interval     = "30s"
              max_failures = 10
            }
          }
        }
        upstreams {
          destination_name = "onos3"
          local_bind_address = "127.0.0.1"
          local_bind_port = 6003
          config {
            connect_timeout_ms = 5000
            limits {
              max_connections         = 3
              max_pending_requests    = 4
              max_concurrent_requests = 5
            }
            passive_health_check {
              interval     = "30s"
              max_failures = 10
            }
          }
        }
      }
    }  
  }
}
