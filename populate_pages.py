import os
import subprocess

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Gaussian-Splatting"
pages_dir = os.path.join(repo_dir, "pages")

pages_content = {
    1: ("The Implicit Ray-Marching Era", "Neural Radiance Fields (NeRFs) introduced the concept of implicit continuous representation for 3D scenes. By mapping spatial coordinates and viewing directions to volume density and RGB color, NeRFs could render novel views using volumetric ray marching.\
\
```mermaid\
graph TD\
  A[Spatial Coords x,y,z] --> C(MLP Network)\
  B[Viewing Direction theta, phi] --> C\
  C --> D[Density & Color]\
  D --> E[Volumetric Ray Marching]\
```"),
    2: ("The Explicit Rasterization Revolution", "3D Gaussian Splatting (3DGS) replaces neural ray marching with an explicit representation of a scene using millions of 3D Gaussians. These are rasterized to screen space using highly parallelized techniques, offering real-time rendering.\
\
```mermaid\
graph LR\
  A[SfM Point Cloud] --> B[Initialize 3D Gaussians]\
  B --> C[Differentiable Tile-based Rasterization]\
  C --> D[Real-time Rendering 100+ FPS]\
```"),
    3: ("The 3D Gaussian Formulation", "Each 3D Gaussian is parameterized by a position, covariance matrix, opacity, and view-dependent color (using Spherical Harmonics). The covariance is decomposed into scaling and rotation components to ensure it remains valid during optimization.\
\
```mermaid\
graph TD\
  A[3D Gaussian Parameterization] --> B[Mean position]\
  A --> C[Covariance (Scale + Rotation)]\
  A --> D[Opacity]\
  A --> E[Spherical Harmonics (Color)]\
```"),
    4: ("Tile-Based Differentiable Rasterization", "The rasterizer projects 3D Gaussians onto the 2D screen by sorting them depth-wise into 16x16 tiles. It then performs alpha blending over the sorted Gaussians to compute the final pixel color quickly and differentiably.\
\
```mermaid\
graph LR\
  A[3D Gaussians] --> B[Project to 2D]\
  B --> C[Bin into 16x16 Screen Tiles]\
  C --> D[Radix Sort by Depth]\
  D --> E[Alpha Blending]\
```"),
    5: ("Dynamic & 4D Gaussian Splatting", "By introducing the time dimension, 4D Gaussian Splatting captures dynamic and moving scenes. Time-varying deformations and velocities are modeled using additional neural fields or Fourier coefficients applied to the Gaussians.\
\
```mermaid\
graph TD\
  A[Static 3D Gaussians] --> B[Deformation Network (t)]\
  B --> C[Shifted & Scaled Gaussians]\
  C --> D[Dynamic Scene Rendering]\
```"),
    6: ("Compressed & Anchor-Based Splatting", "Standard 3DGS consumes massive VRAM. Scaffold-GS and similar methods create sparse anchor points that spawn local Gaussians dynamically, heavily reducing the memory footprint while maintaining quality.\
\
```mermaid\
graph TD\
  A[Sparse Anchor Points] --> B[Predict Local Gaussians]\
  B --> C[Vector Quantization]\
  C --> D[10-20x Memory Reduction]\
```"),
    7: ("The Pop-corn Visual Artifact Boundary", "During adaptive control, Gaussians splitting and cloning can cause visual artifacts like floaters. Methods like SuGaR and 2D-GS align Gaussians to flat 2D surface manifolds to improve surface quality and allow smooth mesh extraction.\
\
```mermaid\
graph LR\
  A[Gaussian Splatting Floaters] --> B[Align to 2D Surface Manifolds]\
  B --> C[Enforce Geometric Consistency]\
  C --> D[Clean Seamless Mesh Extraction]\
```"),
    8: ("The Disk Memory and VRAM Streaming Bottleneck", "Massive Gaussian clouds choke web viewers and VRAM. Hierarchical Level-of-Detail (LOD) trees solve this by downsampling or streaming low-frequency Gaussians for distant views dynamically.\
\
```mermaid\
graph TD\
  A[Massive Scene VRAM Bottleneck] --> B[Hierarchical Octrees]\
  B --> C[Level-of-Detail Streaming]\
  C --> D[Smooth Web & VR Playback]\
```"),
    9: ("Instant Text/Image-to-3D Asset Pipelines", "Integrating multi-view diffusion models with 3DGS allows for near-instant generative 3D asset creation from single images or text prompts, bypassing the long iteration times of NeRF-based generators.\
\
```mermaid\
graph LR\
  A[Text/Image Prompt] --> B[Multi-view Diffusion Model]\
  B --> C[Feed-forward 3DGS Predictor]\
  C --> D[Instant 3D Asset]\
```"),
    10: ("Immersive XR Virtual Production", "Game engines like Unreal Engine and Unity have integrated 3DGS plugins to stream photorealistic captures into virtual production volumes dynamically, replacing traditional green screens.\
\
```mermaid\
graph TD\
  A[Real-world 3DGS Capture] --> B[Unreal Engine Integration]\
  B --> C[Real-time Physical Camera Tracking]\
  C --> D[Interactive XR Volume Rendering]\
```"),
    11: ("Autonomous Driving Simulation", "Using 3DGS to model massive long-range street scenarios from vehicle cameras. Autonomous agents can be safely tested in simulated, hyper-realistic, dynamic 3D environments.\
\
```mermaid\
graph LR\
  A[Multi-camera Vehicle Rig Data] --> B[Long-range 3DGS Scene]\
  B --> C[Simulate Dynamic Obstacles / Weather]\
  C --> D[Closed-loop AV Testing]\
```")
}

for i, (title, text) in pages_content.items():
    content = f"# {title}\
\
{text}\
"
    with open(os.path.join(pages_dir, f"{i}.md"), "w", encoding="utf-8") as f:
        f.write(content)

def run(cmd):
    subprocess.run(["powershell", "-Command", cmd], cwd=repo_dir)

run('git add .')
run('git commit -m "detailed pages created"')
run('git -c http.sslVerify=false push')
