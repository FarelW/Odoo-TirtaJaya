<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Module Addons Odoo</h3>
  <p align="center">
    Module Addons Odoo ini menghadirkan serangkaian ekstensi untuk memperkuat fungsi CRM, otomasi pemasaran, dan pelaporan di Odoo 16. Dengan modul “Marketing Automation Custom” Anda dapat menjadwalkan dan mengirim kampanye e-mail otomatis berdasarkan tahap CRM
  </p>
</div>



<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



## About The Project

### Built With

* [![Odoo][Odoo.com]](https://www.odoo.com/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Git
* Docker
* Docker compose

### Installation

1. Clone repository
   ```sh
   git clone https://github.com/FarelW/Odoo-TirtaJaya.git
   ```
2. Jalankan docker compose
   ```sh
   docker compose up -d --build
   ```
3. Buat database hingga muncul file odoo.conf
4. Ubah file odoo.conf dengan menambahkan addons path
   ```ini
   addons_path = /mnt/extra-addons, /usr/lib/python3/dist-packages/odoo/addons
   ```
5. Install modul custom
    - Masuk ke Odoo sebagai admin
    - Aktifkan Developer Mode (dari menu Settings).
    - Buka Apps, klik tombol Update App List.
    - Install CRM, Email Marketing terlebih dahulu
    - Cari “Marketing Automation Custom” lalu install
    - Di menu akan muncul modul custom


[Odoo.com]: https://img.shields.io/badge/Odoo-714B67?logo=Odoo&logoColor=fff