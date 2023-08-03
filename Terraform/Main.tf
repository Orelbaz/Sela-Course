provider "google" {
  credentials = file("~/home/or/Desktop/gke-Key.json")
  project     = "gke-first-393008"
  region      = "us-central1" 
}

# Include the GKE-Prod and GKE-Test cluster configurations
module "eks_prod_cluster" {
  source = "./GKE-Prod.tf"
}

module "eks_test_cluster" {
  source = "./GKE-Test.tf"
}

