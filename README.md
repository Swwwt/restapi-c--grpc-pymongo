# restapi-c--grpc-pymongo

## Summary

- **Business Service** (C#)
  - Call Data Service to acquire data according to frontend requirements
  - Expose Restful API to frontend
  
- **Data Service** (python)
  - Manage MongoDB using `pymongodb`
  - Expose GRPC interface to Business Service.


## Accomplish

- [x] Build C# client to call Python server
- [x] Expose Restful API in C#
- [x] Use `Postman` in API testing

## Usage

```
python data_service.py
dotnet run
```

**Web API Exposed**
  - *GetApplication*: api/application/?name=app1
  - *PostApplication*: api/application
    - body = {"id": 1, "name": "app1", "description": "The first test", "date": "0213", "creator": "swt"}
  - *DeleteApplication*: api/application/?name=app1
  - *GetUser*: api/application/?name=swt

