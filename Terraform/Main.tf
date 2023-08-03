provider "google" {
  credentials = file("gke-Key.json")
  project     = "gke-first-393008"
  region      = "us-central1"
}

resource "google_container_cluster" "eks_prod" {
  name     = "eks-prod"
  location = "us-central1-c"
  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"
  }

   Optional: Uncomment this block to enable autoscaling for eks-prod
   node_pool {
     autoscaling {
       min_node_count = 1
       max_node_count = 5
     }
   }
}

resource "google_container_cluster" "eks_test" {
  name     = "eks-test"
  location = "us-central1-c"
  initial_node_count = 1

  node_config {
    machine_type = "e2-medium"
  }

   Optional: Uncomment this block to enable autoscaling for eks-test
   node_pool {
     autoscaling {
       min_node_count = 1
       max_node_count = 5
     }
   }
}
