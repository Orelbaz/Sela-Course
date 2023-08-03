# eks_prod_cluster.tf

provider "google" {
  credentials = file("~/home/or/Desktop/gke-Key.json")
  project     = "gke-first-393008"
  region      = "us-central1"
}

resource "google_container_cluster" "eks_prod" {
  name     = "eks-prod"
  location = "us-central1-c"
  initial_node_count = 1
  logging_service   = "logging.googleapis.com/kubernetes"
  monitoring_service = "monitoring.googleapis.com/kubernetes"
  ip_allocation_policy {
    cluster_ipv4_cidr_block = "10.0.0.0/14"
  }
  remove_default_node_pool = true

  node_config {
    machine_type = "e2-medium"
    image_type   = "COS_CONTAINERD"
    disk_type    = "pd-balanced"
    disk_size_gb = 32
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
    tags = ["gke-first-393008"]
    shielded_instance_config {
      enable_secure_boot = false
      enable_integrity_monitoring = true
    }
  }

  network_config {
    network    = "projects/gke-first-393008/global/networks/default"
    subnetwork = "projects/gke-first-393008/regions/us-central1/subnetworks/default"
  }

  location_policy {
    zone_selector = "us-central1-c"
  }

  maintenance_policy {
    window {
      daily_maintenance_window {
        start_time = "02:00"
        recurrence = "FREQ=DAILY"
      }
    }
  }

  addons_config {
    horizontal_pod_autoscaling {
      disabled = false
    }
    http_load_balancing {
      disabled = false
    }
    kubernetes_dashboard {
      disabled = true
    }
    gce_persistent_disk_csi_driver {
      disabled = false
    }
  }

  master_auth {
    username = ""
    password = ""
  }

  enable_tpu = false
}
