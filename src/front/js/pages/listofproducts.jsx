import React from "react";
import BannerProducts from "../../../../public/images/image_480.png";
import "../../styles/listofproducts.css"
import TopProduct from '../component/topproduct.jsx'
const ListOfProducts = () => {
    return (
        <div className="w-100 m-0 p-0 list-of-products-container">
            <div className="banner-container w-100 d-flex" >
            <div className="container-banner-title align-items-center">
                <h1 className="banner-products-title">
                    Nuestros productos
                </h1>
            </div>
        
                <img src={BannerProducts} className="banner-img mb-5" alt="banner-img" />
                </div>
                <div className="container-background align-items-center justify-content-center d-flex mt-5">
                <div className="container background">
  <div className="row d-flex">
    <div className="col-md-4 col-xs-12">
      <TopProduct />
    </div>
    <div className="col-md-4 col-xs-12">
      <TopProduct />
    </div>
    <div className="col-md-4 col-xs-12">
      <TopProduct />
    </div>
  </div>
  
</div>

            </div>
            <div className="btn-container w-100 d-flex justify-content-center">
            <button className="btn-see-more">
              Ver más
            </button>
            </div>
        </div>
       
    )
}

export default ListOfProducts;