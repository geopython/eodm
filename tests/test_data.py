from pystac import Collection, Item

STAC_ITEMS = list(
    Item.from_dict(item)
    for item in [
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "S2A_39QTA_20230628_0_L2A",
            "properties": {
                "created": "2023-06-28T15:42:10.537Z",
                "platform": "sentinel-2a",
                "constellation": "sentinel-2",
                "instruments": ["msi"],
                "eo:cloud_cover": 4.025136,
                "proj:epsg": 32639,
                "mgrs:utm_zone": 39,
                "mgrs:latitude_band": "Q",
                "mgrs:grid_square": "TA",
                "grid:code": "MGRS-39QTA",
                "view:sun_azimuth": 72.5914543525993,
                "view:sun_elevation": 69.8613692052989,
                "s2:degraded_msi_data_percentage": 0,
                "s2:nodata_pixel_percentage": 0,
                "s2:saturated_defective_pixel_percentage": 0,
                "s2:dark_features_percentage": 0,
                "s2:cloud_shadow_percentage": 0,
                "s2:vegetation_percentage": 0,
                "s2:not_vegetated_percentage": 95.974845,
                "s2:water_percentage": 0,
                "s2:unclassified_percentage": 2e-05,
                "s2:medium_proba_clouds_percentage": 0.128606,
                "s2:high_proba_clouds_percentage": 0.132266,
                "s2:thin_cirrus_percentage": 3.764264,
                "s2:snow_ice_percentage": 0,
                "s2:product_type": "S2MSI2A",
                "s2:processing_baseline": "05.09",
                "s2:product_uri": "S2A_MSIL2A_20230628T070631_N0509_R106_T39QTA_20230628T113955.SAFE",
                "s2:generation_time": "2023-06-28T11:39:55.000000Z",
                "s2:datatake_id": "GS2A_20230628T070631_041859_N05.09",
                "s2:datatake_type": "INS-NOBS",
                "s2:datastrip_id": "S2A_OPER_MSI_L2A_DS_2APS_20230628T113955_S20230628T071848_N05.09",
                "s2:granule_id": "S2A_OPER_MSI_L2A_TL_2APS_20230628T113955_A041859_T39QTA_N05.09",
                "s2:reflectance_conversion_factor": 0.967915542603869,
                "datetime": "2023-06-28T07:24:41.632000Z",
                "s2:sequence": "0",
                "earthsearch:s3_path": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A",
                "earthsearch:payload_id": "roda-sentinel2/workflow-sentinel2-to-stac/08df7afa5bd2122b76659edafeca15e5",
                "earthsearch:boa_offset_applied": True,
                "processing:software": {"sentinel2-to-stac": "0.1.0"},
                "updated": "2023-06-28T15:42:10.537Z",
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [48.15089336343958, 18.970584163790633],
                        [49.193086478160915, 18.983692366107967],
                        [49.20345625325104, 17.991811740910624],
                        [48.16722825280431, 17.97943517464906],
                        [48.15089336343958, 18.970584163790633],
                    ]
                ],
            },
            "links": [
                {
                    "rel": "self",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_39QTA_20230628_0_L2A",
                    "type": "application/geo+json",
                },
                {
                    "rel": "canonical",
                    "href": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/S2A_39QTA_20230628_0_L2A.json",
                    "type": "application/json",
                },
                {
                    "rel": "license",
                    "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice",
                },
                {
                    "rel": "derived_from",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items/S2A_39QTA_20230628_0_L1C",
                    "type": "application/geo+json",
                },
                {
                    "rel": "parent",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "collection",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "root",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                    "title": "Earth Search by Element 84",
                },
                {
                    "rel": "thumbnail",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_39QTA_20230628_0_L2A/thumbnail",
                },
            ],
            "assets": {
                "aot": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/AOT.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B02.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B01.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "granule_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/granule_metadata.xml",
                    "type": "application/xml",
                    "roles": ["metadata"],
                },
                "green": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B03.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B08.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B8A.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B09.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B04.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B05.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B06.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B07.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/SCL.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B11.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/B12.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "thumbnail": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/thumbnail.jpg",
                    "type": "image/jpeg",
                    "title": "Thumbnail image",
                    "roles": ["thumbnail"],
                },
                "tileinfo_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/tileinfo_metadata.json",
                    "type": "application/json",
                    "roles": ["metadata"],
                },
                "visual": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/TCI.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2A_39QTA_20230628_0_L2A/WVP.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "aot-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/AOT.jp2",
                    "type": "image/jp2",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B02.jp2",
                    "type": "image/jp2",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B01.jp2",
                    "type": "image/jp2",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "green-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B03.jp2",
                    "type": "image/jp2",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B08.jp2",
                    "type": "image/jp2",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B8A.jp2",
                    "type": "image/jp2",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B09.jp2",
                    "type": "image/jp2",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B04.jp2",
                    "type": "image/jp2",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B05.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B06.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B07.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/SCL.jp2",
                    "type": "image/jp2",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B11.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/B12.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "visual-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/TCI.jp2",
                    "type": "image/jp2",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/28/0/WVP.jp2",
                    "type": "image/jp2",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
            },
            "bbox": [
                48.15089336343958,
                17.97943517464906,
                49.20345625325104,
                18.983692366107967,
            ],
            "stac_extensions": [
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",
                "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
                "https://stac-extensions.github.io/grid/v1.0.0/schema.json",
                "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
                "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
                "https://stac-extensions.github.io/mgrs/v1.0.0/schema.json",
            ],
            "collection": "sentinel-2-l2a",
        },
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "S2A_39QUA_20230628_0_L2A",
            "properties": {
                "created": "2023-06-28T15:36:17.131Z",
                "platform": "sentinel-2a",
                "constellation": "sentinel-2",
                "instruments": ["msi"],
                "eo:cloud_cover": 4.255069,
                "proj:epsg": 32639,
                "mgrs:utm_zone": 39,
                "mgrs:latitude_band": "Q",
                "mgrs:grid_square": "UA",
                "grid:code": "MGRS-39QUA",
                "view:sun_azimuth": 72.1630075034592,
                "view:sun_elevation": 70.7095029637061,
                "s2:degraded_msi_data_percentage": 0.012,
                "s2:nodata_pixel_percentage": 0,
                "s2:saturated_defective_pixel_percentage": 0,
                "s2:dark_features_percentage": 0,
                "s2:cloud_shadow_percentage": 0,
                "s2:vegetation_percentage": 0,
                "s2:not_vegetated_percentage": 95.74489,
                "s2:water_percentage": 0,
                "s2:unclassified_percentage": 4e-05,
                "s2:medium_proba_clouds_percentage": 0.044847,
                "s2:high_proba_clouds_percentage": 0.004691,
                "s2:thin_cirrus_percentage": 4.20553,
                "s2:snow_ice_percentage": 0,
                "s2:product_type": "S2MSI2A",
                "s2:processing_baseline": "05.09",
                "s2:product_uri": "S2A_MSIL2A_20230628T070631_N0509_R106_T39QUA_20230628T113955.SAFE",
                "s2:generation_time": "2023-06-28T11:39:55.000000Z",
                "s2:datatake_id": "GS2A_20230628T070631_041859_N05.09",
                "s2:datatake_type": "INS-NOBS",
                "s2:datastrip_id": "S2A_OPER_MSI_L2A_DS_2APS_20230628T113955_S20230628T071848_N05.09",
                "s2:granule_id": "S2A_OPER_MSI_L2A_TL_2APS_20230628T113955_A041859_T39QUA_N05.09",
                "s2:reflectance_conversion_factor": 0.967915542603869,
                "datetime": "2023-06-28T07:24:38.255000Z",
                "s2:sequence": "0",
                "earthsearch:s3_path": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A",
                "earthsearch:payload_id": "roda-sentinel2/workflow-sentinel2-to-stac/ef07819884c3850977fd8d076c176664",
                "earthsearch:boa_offset_applied": True,
                "processing:software": {"sentinel2-to-stac": "0.1.0"},
                "updated": "2023-06-28T15:36:17.131Z",
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [49.10024193711239, 18.98276267726576],
                        [50.1430563241428, 18.99052878648329],
                        [50.14797678232211, 17.998266544949992],
                        [49.11114378622382, 17.990933946147493],
                        [49.10024193711239, 18.98276267726576],
                    ]
                ],
            },
            "links": [
                {
                    "rel": "self",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_39QUA_20230628_0_L2A",
                    "type": "application/geo+json",
                },
                {
                    "rel": "canonical",
                    "href": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/S2A_39QUA_20230628_0_L2A.json",
                    "type": "application/json",
                },
                {
                    "rel": "license",
                    "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice",
                },
                {
                    "rel": "derived_from",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items/S2A_39QUA_20230628_0_L1C",
                    "type": "application/geo+json",
                },
                {
                    "rel": "parent",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "collection",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "root",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                    "title": "Earth Search by Element 84",
                },
                {
                    "rel": "thumbnail",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2A_39QUA_20230628_0_L2A/thumbnail",
                },
            ],
            "assets": {
                "aot": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/AOT.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B02.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B01.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 300000, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "granule_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/granule_metadata.xml",
                    "type": "application/xml",
                    "roles": ["metadata"],
                },
                "green": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B03.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B08.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B8A.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B09.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 300000, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B04.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B05.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B06.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B07.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/SCL.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B11.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/B12.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "thumbnail": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/thumbnail.jpg",
                    "type": "image/jpeg",
                    "title": "Thumbnail image",
                    "roles": ["thumbnail"],
                },
                "tileinfo_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/tileinfo_metadata.json",
                    "type": "application/json",
                    "roles": ["metadata"],
                },
                "visual": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/TCI.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/UA/2023/6/S2A_39QUA_20230628_0_L2A/WVP.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "aot-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/AOT.jp2",
                    "type": "image/jp2",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B02.jp2",
                    "type": "image/jp2",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B01.jp2",
                    "type": "image/jp2",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 300000, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "green-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B03.jp2",
                    "type": "image/jp2",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B08.jp2",
                    "type": "image/jp2",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B8A.jp2",
                    "type": "image/jp2",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B09.jp2",
                    "type": "image/jp2",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 300000, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B04.jp2",
                    "type": "image/jp2",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B05.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B06.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B07.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/SCL.jp2",
                    "type": "image/jp2",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B11.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/B12.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "visual-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/TCI.jp2",
                    "type": "image/jp2",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 300000, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/UA/2023/6/28/0/WVP.jp2",
                    "type": "image/jp2",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 300000, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
            },
            "bbox": [
                49.10024193711239,
                17.990933946147493,
                50.14797678232211,
                18.99052878648329,
            ],
            "stac_extensions": [
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",
                "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
                "https://stac-extensions.github.io/mgrs/v1.0.0/schema.json",
                "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
                "https://stac-extensions.github.io/grid/v1.0.0/schema.json",
                "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
            ],
            "collection": "sentinel-2-l2a",
        },
        {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": "S2B_39QTA_20230623_0_L2A",
            "properties": {
                "created": "2023-06-23T16:52:42.543Z",
                "platform": "sentinel-2b",
                "constellation": "sentinel-2",
                "instruments": ["msi"],
                "eo:cloud_cover": 0,
                "proj:epsg": 32639,
                "mgrs:utm_zone": 39,
                "mgrs:latitude_band": "Q",
                "mgrs:grid_square": "TA",
                "grid:code": "MGRS-39QTA",
                "view:sun_azimuth": 72.0519933214079,
                "view:sun_elevation": 70.0748719362623,
                "s2:degraded_msi_data_percentage": 0.0212,
                "s2:nodata_pixel_percentage": 0,
                "s2:saturated_defective_pixel_percentage": 0,
                "s2:dark_features_percentage": 0,
                "s2:cloud_shadow_percentage": 0,
                "s2:vegetation_percentage": 0,
                "s2:not_vegetated_percentage": 100,
                "s2:water_percentage": 0,
                "s2:unclassified_percentage": 0,
                "s2:medium_proba_clouds_percentage": 0,
                "s2:high_proba_clouds_percentage": 0,
                "s2:thin_cirrus_percentage": 0,
                "s2:snow_ice_percentage": 0,
                "s2:product_type": "S2MSI2A",
                "s2:processing_baseline": "05.09",
                "s2:product_uri": "S2B_MSIL2A_20230623T070629_N0509_R106_T39QTA_20230623T101205.SAFE",
                "s2:generation_time": "2023-06-23T10:12:05.000000Z",
                "s2:datatake_id": "GS2B_20230623T070629_032879_N05.09",
                "s2:datatake_type": "INS-NOBS",
                "s2:datastrip_id": "S2B_OPER_MSI_L2A_DS_2BPS_20230623T101205_S20230623T072412_N05.09",
                "s2:granule_id": "S2B_OPER_MSI_L2A_TL_2BPS_20230623T101205_A032879_T39QTA_N05.09",
                "s2:reflectance_conversion_factor": 0.968539891755911,
                "datetime": "2023-06-23T07:24:41.575000Z",
                "s2:sequence": "0",
                "earthsearch:s3_path": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A",
                "earthsearch:payload_id": "roda-sentinel2/workflow-sentinel2-to-stac/331e8f93a9cbeee37f0cf9d89d061d56",
                "earthsearch:boa_offset_applied": True,
                "processing:software": {"sentinel2-to-stac": "0.1.0"},
                "updated": "2023-06-23T16:52:42.543Z",
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [48.15089336343958, 18.970584163790633],
                        [49.193086478160915, 18.983692366107967],
                        [49.20345625325104, 17.991811740910624],
                        [48.16722825280431, 17.97943517464906],
                        [48.15089336343958, 18.970584163790633],
                    ]
                ],
            },
            "links": [
                {
                    "rel": "self",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2B_39QTA_20230623_0_L2A",
                    "type": "application/geo+json",
                },
                {
                    "rel": "canonical",
                    "href": "s3://sentinel-cogs/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/S2B_39QTA_20230623_0_L2A.json",
                    "type": "application/json",
                },
                {
                    "rel": "license",
                    "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice",
                },
                {
                    "rel": "derived_from",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items/S2B_39QTA_20230623_0_L1C",
                    "type": "application/geo+json",
                },
                {
                    "rel": "parent",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "collection",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "root",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                    "title": "Earth Search by Element 84",
                },
                {
                    "rel": "thumbnail",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items/S2B_39QTA_20230623_0_L2A/thumbnail",
                },
            ],
            "assets": {
                "aot": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/AOT.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B02.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B01.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "granule_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/granule_metadata.xml",
                    "type": "application/xml",
                    "roles": ["metadata"],
                },
                "green": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B03.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B08.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B8A.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B09.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B04.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B05.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B06.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B07.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/SCL.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B11.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/B12.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "thumbnail": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/thumbnail.jpg",
                    "type": "image/jpeg",
                    "title": "Thumbnail image",
                    "roles": ["thumbnail"],
                },
                "tileinfo_metadata": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/tileinfo_metadata.json",
                    "type": "application/json",
                    "roles": ["metadata"],
                },
                "visual": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/TCI.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp": {
                    "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/39/Q/TA/2023/6/S2B_39QTA_20230623_0_L2A/WVP.tif",
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "aot-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/AOT.jp2",
                    "type": "image/jp2",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B02.jp2",
                    "type": "image/jp2",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B01.jp2",
                    "type": "image/jp2",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "green-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B03.jp2",
                    "type": "image/jp2",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B08.jp2",
                    "type": "image/jp2",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B8A.jp2",
                    "type": "image/jp2",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B09.jp2",
                    "type": "image/jp2",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 199980, 0, -60, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B04.jp2",
                    "type": "image/jp2",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B05.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B06.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B07.jp2",
                    "type": "image/jp2",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/SCL.jp2",
                    "type": "image/jp2",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B11.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/B12.jp2",
                    "type": "image/jp2",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": -0.1,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "visual-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/TCI.jp2",
                    "type": "image/jp2",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 199980, 0, -10, 2100000],
                    "roles": ["visual"],
                },
                "wvp-jp2": {
                    "href": "s3://sentinel-s2-l2a/tiles/39/Q/TA/2023/6/23/0/WVP.jp2",
                    "type": "image/jp2",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 199980, 0, -20, 2100000],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
            },
            "bbox": [
                48.15089336343958,
                17.97943517464906,
                49.20345625325104,
                18.983692366107967,
            ],
            "stac_extensions": [
                "https://stac-extensions.github.io/projection/v1.0.0/schema.json",
                "https://stac-extensions.github.io/grid/v1.0.0/schema.json",
                "https://stac-extensions.github.io/mgrs/v1.0.0/schema.json",
                "https://stac-extensions.github.io/processing/v1.1.0/schema.json",
                "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
                "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",
            ],
            "collection": "sentinel-2-l2a",
        },
    ]
)

STAC_COLLECTIONS = list(
    Collection.from_dict(collection)
    for collection in [
        {
            "type": "Collection",
            "id": "sentinel-2-l2a",
            "stac_version": "1.0.0",
            "description": "Global Sentinel-2 data from the Multispectral Instrument (MSI) onboard Sentinel-2",
            "links": [
                {
                    "rel": "self",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a",
                    "type": "application/json",
                },
                {
                    "rel": "cite-as",
                    "href": "https://doi.org/10.5270/S2_-742ikth",
                    "title": "Copernicus Sentinel-2 MSI Level-2A (L2A) Bottom-of-Atmosphere Radiance",
                },
                {
                    "rel": "license",
                    "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice",
                    "title": "proprietary",
                },
                {
                    "rel": "parent",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                },
                {
                    "rel": "root",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                    "title": "Earth Search by Element 84",
                },
                {
                    "rel": "items",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/items",
                    "type": "application/geo+json",
                },
                {
                    "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/queryables",
                    "type": "application/schema+json",
                },
                {
                    "rel": "aggregate",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/aggregate",
                    "type": "application/json",
                    "method": "GET",
                },
                {
                    "rel": "aggregations",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l2a/aggregations",
                    "type": "application/json",
                },
            ],
            "stac_extensions": [
                "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
                "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
            ],
            "item_assets": {
                "aot": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "granule_metadata": {"type": "application/xml", "roles": ["metadata"]},
                "green": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "thumbnail": {
                    "type": "image/jpeg",
                    "title": "Thumbnail image",
                    "roles": ["thumbnail"],
                },
                "tileinfo_metadata": {"type": "application/json", "roles": ["metadata"]},
                "visual": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "roles": ["visual"],
                },
                "wvp": {
                    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "aot-jp2": {
                    "type": "image/jp2",
                    "title": "Aerosol optical thickness (AOT)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "blue-jp2": {
                    "type": "image/jp2",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal-jp2": {
                    "type": "image/jp2",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "green-jp2": {
                    "type": "image/jp2",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir-jp2": {
                    "type": "image/jp2",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08-jp2": {
                    "type": "image/jp2",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09-jp2": {
                    "type": "image/jp2",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red-jp2": {
                    "type": "image/jp2",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1-jp2": {
                    "type": "image/jp2",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2-jp2": {
                    "type": "image/jp2",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3-jp2": {
                    "type": "image/jp2",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "scl-jp2": {
                    "type": "image/jp2",
                    "title": "Scene classification map (SCL)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {"nodata": 0, "data_type": "uint8", "spatial_resolution": 20}
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16-jp2": {
                    "type": "image/jp2",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22-jp2": {
                    "type": "image/jp2",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "visual-jp2": {
                    "type": "image/jp2",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "roles": ["visual"],
                },
                "wvp-jp2": {
                    "type": "image/jp2",
                    "title": "Water vapour (WVP)",
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "unit": "cm",
                            "scale": 0.001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
            },
            "title": "Sentinel-2 Level-2A",
            "extent": {
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [["2015-06-27T10:25:31.456000Z", None]]},
            },
            "license": "proprietary",
            "keywords": ["sentinel", "earth observation", "esa"],
            "providers": [
                {
                    "name": "ESA",
                    "roles": ["producer"],
                    "url": "https://earth.esa.int/web/guest/home",
                },
                {
                    "name": "Sinergise",
                    "roles": ["processor"],
                    "url": "https://registry.opendata.aws/sentinel-2/",
                },
                {
                    "name": "AWS",
                    "roles": ["host"],
                    "url": "http://sentinel-pds.s3-website.eu-central-1.amazonaws.com/",
                },
                {
                    "name": "Element 84",
                    "roles": ["processor"],
                    "url": "https://element84.com",
                },
            ],
            "summaries": {
                "platform": ["sentinel-2a", "sentinel-2b"],
                "constellation": ["sentinel-2"],
                "instruments": ["msi"],
                "gsd": [10, 20, 60],
                "view:off_nadir": [0],
                "sci:doi": ["10.5270/s2_-znk9xsj"],
                "eo:bands": [
                    {
                        "name": "coastal",
                        "common_name": "coastal",
                        "description": "Coastal aerosol (band 1)",
                        "center_wavelength": 0.443,
                        "full_width_half_max": 0.027,
                    },
                    {
                        "name": "blue",
                        "common_name": "blue",
                        "description": "Blue (band 2)",
                        "center_wavelength": 0.49,
                        "full_width_half_max": 0.098,
                    },
                    {
                        "name": "green",
                        "common_name": "green",
                        "description": "Green (band 3)",
                        "center_wavelength": 0.56,
                        "full_width_half_max": 0.045,
                    },
                    {
                        "name": "red",
                        "common_name": "red",
                        "description": "Red (band 4)",
                        "center_wavelength": 0.665,
                        "full_width_half_max": 0.038,
                    },
                    {
                        "name": "rededge1",
                        "common_name": "rededge",
                        "description": "Red edge 1 (band 5)",
                        "center_wavelength": 0.704,
                        "full_width_half_max": 0.019,
                    },
                    {
                        "name": "rededge2",
                        "common_name": "rededge",
                        "description": "Red edge 2 (band 6)",
                        "center_wavelength": 0.74,
                        "full_width_half_max": 0.018,
                    },
                    {
                        "name": "rededge3",
                        "common_name": "rededge",
                        "description": "Red edge 3 (band 7)",
                        "center_wavelength": 0.783,
                        "full_width_half_max": 0.028,
                    },
                    {
                        "name": "nir",
                        "common_name": "nir",
                        "description": "NIR 1 (band 8)",
                        "center_wavelength": 0.842,
                        "full_width_half_max": 0.145,
                    },
                    {
                        "name": "nir08",
                        "common_name": "nir08",
                        "description": "NIR 2 (band 8A)",
                        "center_wavelength": 0.865,
                        "full_width_half_max": 0.033,
                    },
                    {
                        "name": "nir09",
                        "common_name": "nir09",
                        "description": "NIR 3 (band 9)",
                        "center_wavelength": 0.945,
                        "full_width_half_max": 0.026,
                    },
                    {
                        "name": "cirrus",
                        "common_name": "cirrus",
                        "description": "Cirrus (band 10)",
                        "center_wavelength": 1.3735,
                        "full_width_half_max": 0.075,
                    },
                    {
                        "name": "swir16",
                        "common_name": "swir16",
                        "description": "SWIR 1 (band 11)",
                        "center_wavelength": 1.61,
                        "full_width_half_max": 0.143,
                    },
                    {
                        "name": "swir22",
                        "common_name": "swir22",
                        "description": "SWIR 2 (band 12)",
                        "center_wavelength": 2.19,
                        "full_width_half_max": 0.242,
                    },
                ],
            },
        },
        {
            "type": "Collection",
            "id": "sentinel-2-l1c",
            "stac_version": "1.0.0",
            "description": "Global Sentinel-2 data from the Multispectral Instrument (MSI) onboard Sentinel-2",
            "links": [
                {
                    "rel": "self",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c",
                    "type": "application/json",
                },
                {
                    "rel": "cite-as",
                    "href": "https://doi.org/10.5270/S2_-742ikth",
                    "title": "Copernicus Sentinel-2 MSI Level-1C (L1C) Top-of-Atmosphere Reflectance",
                },
                {
                    "rel": "license",
                    "href": "https://sentinel.esa.int/documents/247904/690755/Sentinel_Data_Legal_Notice",
                    "title": "proprietary",
                },
                {
                    "rel": "parent",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                },
                {
                    "rel": "root",
                    "href": "https://earth-search.aws.element84.com/v1",
                    "type": "application/json",
                    "title": "Earth Search by Element 84",
                },
                {
                    "rel": "items",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/items",
                    "type": "application/geo+json",
                },
                {
                    "rel": "http://www.opengis.net/def/rel/ogc/1.0/queryables",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/queryables",
                    "type": "application/schema+json",
                },
                {
                    "rel": "aggregate",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/aggregate",
                    "type": "application/json",
                    "method": "GET",
                },
                {
                    "rel": "aggregations",
                    "href": "https://earth-search.aws.element84.com/v1/collections/sentinel-2-l1c/aggregations",
                    "type": "application/json",
                },
            ],
            "stac_extensions": [
                "https://stac-extensions.github.io/item-assets/v1.0.0/schema.json",
                "https://stac-extensions.github.io/view/v1.0.0/schema.json",
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json",
                "https://stac-extensions.github.io/raster/v1.1.0/schema.json",
                "https://stac-extensions.github.io/eo/v1.0.0/schema.json",
            ],
            "item_assets": {
                "blue": {
                    "type": "image/jp2",
                    "title": "Blue (band 2) - 10m",
                    "eo:bands": [
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "cirrus": {
                    "type": "image/jp2",
                    "title": "Cirrus (band 10) - 60m",
                    "eo:bands": [
                        {
                            "name": "cirrus",
                            "common_name": "cirrus",
                            "description": "Cirrus (band 10)",
                            "center_wavelength": 1.3735,
                            "full_width_half_max": 0.075,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "coastal": {
                    "type": "image/jp2",
                    "title": "Coastal aerosol (band 1) - 60m",
                    "eo:bands": [
                        {
                            "name": "coastal",
                            "common_name": "coastal",
                            "description": "Coastal aerosol (band 1)",
                            "center_wavelength": 0.443,
                            "full_width_half_max": 0.027,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "granule_metadata": {"type": "application/xml", "roles": ["metadata"]},
                "green": {
                    "type": "image/jp2",
                    "title": "Green (band 3) - 10m",
                    "eo:bands": [
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir": {
                    "type": "image/jp2",
                    "title": "NIR 1 (band 8) - 10m",
                    "eo:bands": [
                        {
                            "name": "nir",
                            "common_name": "nir",
                            "description": "NIR 1 (band 8)",
                            "center_wavelength": 0.842,
                            "full_width_half_max": 0.145,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir08": {
                    "type": "image/jp2",
                    "title": "NIR 2 (band 8A) - 20m",
                    "eo:bands": [
                        {
                            "name": "nir08",
                            "common_name": "nir08",
                            "description": "NIR 2 (band 8A)",
                            "center_wavelength": 0.865,
                            "full_width_half_max": 0.033,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "nir09": {
                    "type": "image/jp2",
                    "title": "NIR 3 (band 9) - 60m",
                    "eo:bands": [
                        {
                            "name": "nir09",
                            "common_name": "nir09",
                            "description": "NIR 3 (band 9)",
                            "center_wavelength": 0.945,
                            "full_width_half_max": 0.026,
                        }
                    ],
                    "gsd": 60,
                    "proj:shape": [1830, 1830],
                    "proj:transform": [60, 0, 399960, 0, -60, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 60,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "red": {
                    "type": "image/jp2",
                    "title": "Red (band 4) - 10m",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        }
                    ],
                    "gsd": 10,
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 10,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge1": {
                    "type": "image/jp2",
                    "title": "Red edge 1 (band 5) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge1",
                            "common_name": "rededge",
                            "description": "Red edge 1 (band 5)",
                            "center_wavelength": 0.704,
                            "full_width_half_max": 0.019,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge2": {
                    "type": "image/jp2",
                    "title": "Red edge 2 (band 6) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge2",
                            "common_name": "rededge",
                            "description": "Red edge 2 (band 6)",
                            "center_wavelength": 0.74,
                            "full_width_half_max": 0.018,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "rededge3": {
                    "type": "image/jp2",
                    "title": "Red edge 3 (band 7) - 20m",
                    "eo:bands": [
                        {
                            "name": "rededge3",
                            "common_name": "rededge",
                            "description": "Red edge 3 (band 7)",
                            "center_wavelength": 0.783,
                            "full_width_half_max": 0.028,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir16": {
                    "type": "image/jp2",
                    "title": "SWIR 1 (band 11) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir16",
                            "common_name": "swir16",
                            "description": "SWIR 1 (band 11)",
                            "center_wavelength": 1.61,
                            "full_width_half_max": 0.143,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "swir22": {
                    "type": "image/jp2",
                    "title": "SWIR 2 (band 12) - 20m",
                    "eo:bands": [
                        {
                            "name": "swir22",
                            "common_name": "swir22",
                            "description": "SWIR 2 (band 12)",
                            "center_wavelength": 2.19,
                            "full_width_half_max": 0.242,
                        }
                    ],
                    "gsd": 20,
                    "proj:shape": [5490, 5490],
                    "proj:transform": [20, 0, 399960, 0, -20, 4900020],
                    "raster:bands": [
                        {
                            "nodata": 0,
                            "data_type": "uint16",
                            "bits_per_sample": 15,
                            "spatial_resolution": 20,
                            "scale": 0.0001,
                            "offset": 0,
                        }
                    ],
                    "roles": ["data", "reflectance"],
                },
                "thumbnail": {
                    "type": "image/jpeg",
                    "title": "Thumbnail image",
                    "roles": ["thumbnail"],
                },
                "tileinfo_metadata": {"type": "application/json", "roles": ["metadata"]},
                "visual": {
                    "type": "image/jp2",
                    "title": "True color image",
                    "eo:bands": [
                        {
                            "name": "red",
                            "common_name": "red",
                            "description": "Red (band 4)",
                            "center_wavelength": 0.665,
                            "full_width_half_max": 0.038,
                        },
                        {
                            "name": "green",
                            "common_name": "green",
                            "description": "Green (band 3)",
                            "center_wavelength": 0.56,
                            "full_width_half_max": 0.045,
                        },
                        {
                            "name": "blue",
                            "common_name": "blue",
                            "description": "Blue (band 2)",
                            "center_wavelength": 0.49,
                            "full_width_half_max": 0.098,
                        },
                    ],
                    "proj:shape": [10980, 10980],
                    "proj:transform": [10, 0, 399960, 0, -10, 4900020],
                    "roles": ["visual"],
                },
            },
            "title": "Sentinel-2 Level-1C",
            "extent": {
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [["2015-06-27T10:25:31.456000Z", None]]},
            },
            "license": "proprietary",
            "keywords": ["sentinel", "earth observation", "esa"],
            "providers": [
                {
                    "name": "ESA",
                    "roles": ["producer"],
                    "url": "https://earth.esa.int/web/guest/home",
                },
                {
                    "name": "Sinergise",
                    "roles": ["processor"],
                    "url": "https://registry.opendata.aws/sentinel-2/",
                },
                {
                    "name": "AWS",
                    "roles": ["host"],
                    "url": "http://sentinel-pds.s3-website.eu-central-1.amazonaws.com/",
                },
                {
                    "name": "Element 84",
                    "roles": ["processor"],
                    "url": "https://element84.com",
                },
            ],
            "summaries": {
                "platform": ["sentinel-2a", "sentinel-2b"],
                "constellation": ["sentinel-2"],
                "instruments": ["msi"],
                "gsd": [10, 20, 60],
                "view:off_nadir": [0],
                "sci:doi": ["10.5270/s2_-znk9xsj"],
                "eo:bands": [
                    {
                        "name": "coastal",
                        "common_name": "coastal",
                        "description": "Coastal aerosol (band 1)",
                        "center_wavelength": 0.443,
                        "full_width_half_max": 0.027,
                    },
                    {
                        "name": "blue",
                        "common_name": "blue",
                        "description": "Blue (band 2)",
                        "center_wavelength": 0.49,
                        "full_width_half_max": 0.098,
                    },
                    {
                        "name": "green",
                        "common_name": "green",
                        "description": "Green (band 3)",
                        "center_wavelength": 0.56,
                        "full_width_half_max": 0.045,
                    },
                    {
                        "name": "red",
                        "common_name": "red",
                        "description": "Red (band 4)",
                        "center_wavelength": 0.665,
                        "full_width_half_max": 0.038,
                    },
                    {
                        "name": "rededge1",
                        "common_name": "rededge",
                        "description": "Red edge 1 (band 5)",
                        "center_wavelength": 0.704,
                        "full_width_half_max": 0.019,
                    },
                    {
                        "name": "rededge2",
                        "common_name": "rededge",
                        "description": "Red edge 2 (band 6)",
                        "center_wavelength": 0.74,
                        "full_width_half_max": 0.018,
                    },
                    {
                        "name": "rededge3",
                        "common_name": "rededge",
                        "description": "Red edge 3 (band 7)",
                        "center_wavelength": 0.783,
                        "full_width_half_max": 0.028,
                    },
                    {
                        "name": "nir",
                        "common_name": "nir",
                        "description": "NIR 1 (band 8)",
                        "center_wavelength": 0.842,
                        "full_width_half_max": 0.145,
                    },
                    {
                        "name": "nir08",
                        "common_name": "nir08",
                        "description": "NIR 2 (band 8A)",
                        "center_wavelength": 0.865,
                        "full_width_half_max": 0.033,
                    },
                    {
                        "name": "nir09",
                        "common_name": "nir09",
                        "description": "NIR 3 (band 9)",
                        "center_wavelength": 0.945,
                        "full_width_half_max": 0.026,
                    },
                    {
                        "name": "cirrus",
                        "common_name": "cirrus",
                        "description": "Cirrus (band 10)",
                        "center_wavelength": 1.3735,
                        "full_width_half_max": 0.075,
                    },
                    {
                        "name": "swir16",
                        "common_name": "swir16",
                        "description": "SWIR 1 (band 11)",
                        "center_wavelength": 1.61,
                        "full_width_half_max": 0.143,
                    },
                    {
                        "name": "swir22",
                        "common_name": "swir22",
                        "description": "SWIR 2 (band 12)",
                        "center_wavelength": 2.19,
                        "full_width_half_max": 0.242,
                    },
                ],
            },
        },
    ]
)
