# `lunarclient.websocket.performance.v1`

## Service `PerformanceService`

Source: [`proto/extracted/lunarclient_websocket_performance_v1_service.proto`](../../proto/extracted/lunarclient_websocket_performance_v1_service.proto)

| Method | Request | Response |
|---|---|---|
| `RecordPerfSnapshot` | `lunarclient.websocket.performance.v1.RecordPerfSnapshotRequest` | `lunarclient.websocket.performance.v1.RecordPerfSnapshotResponse` |
| `StartJfrUpload` | `lunarclient.websocket.performance.v1.StartJfrUploadRequest` | `lunarclient.websocket.performance.v1.StartJfrUploadResponse` |
| `CompleteJfrUpload` | `lunarclient.websocket.performance.v1.CompleteJfrUploadRequest` | `lunarclient.websocket.performance.v1.CompleteJfrUploadResponse` |

## Enums

- enum **GraphicsStatus**:
  - `GRAPHICS_STATUS_UNSPECIFIED = 0`
  - `GRAPHICS_STATUS_FANCY = 1`
  - `GRAPHICS_STATUS_FAST = 2`
  - `GRAPHICS_STATUS_FABULOUS = 3`
- enum **ChunkBuilder**:
  - `CHUNK_BUILDER_UNSPECIFIED = 0`
  - `CHUNK_BUILDER_THREADED = 1`
  - `CHUNK_BUILDER_SEMI_BLOCKING = 2`
  - `CHUNK_BUILDER_FULLY_BLOCKING = 3`
- enum **CloudsMode**:
  - `CLOUDS_MODE_UNSPECIFIED = 0`
  - `CLOUDS_MODE_FANCY = 1`
  - `CLOUDS_MODE_FAST = 2`
  - `CLOUDS_MODE_OFF = 3`
- enum **ParticlesMode**:
  - `PARTICLES_MODE_UNSPECIFIED = 0`
  - `PARTICLES_MODE_ALL = 1`
  - `PARTICLES_MODE_DECREASED = 2`
  - `PARTICLES_MODE_MINIMAL = 3`
- enum **LazyChunkLoading**:
  - `LAZY_CHUNK_LOADING_UNSPECIFIED = 0`
  - `LAZY_CHUNK_LOADING_MEDIUM = 1`
  - `LAZY_CHUNK_LOADING_VANILLA = 2`
  - `LAZY_CHUNK_LOADING_HIGH = 3`
  - `LAZY_CHUNK_LOADING_LOW = 4`
  - `LAZY_CHUNK_LOADING_LOWEST = 5`
  - `LAZY_CHUNK_LOADING_HIGHEST = 6`
- enum **TextureFiltering**:
  - `TEXTURE_FILTERING_NONE_UNSPECIFIED = 0`
  - `TEXTURE_FILTERING_RGSS = 1`
  - `TEXTURE_FILTERING_ANISOTROPIC = 2`

## Messages

- **RecordPerfSnapshotRequest**
- **AverageGroup**
  - `float` `average` = 1
  - `int32` `high` = 2
  - `int32` `low` = 3
- **NvidiaGpuMemoryState**
  - `int32` `current_available_vram_kb` = 1
  - `int32` `evicted_memory_kb` = 2
- **AmdGpuMemoryState**
  - `int32` `vbo_total_pool_available_kb` = 1
  - `int32` `vbo_largest_available_free_block_kb` = 2
  - `int32` `vbo_total_auxiliary_memory_free_kb` = 3
  - `int32` `vbo_largest_auxiliary_free_block_kb` = 4
- **RecordPerfSnapshotResponse**
- **StartJfrUploadRequest**
  - repeated `lunarclient.websocket.performance.v1.StartJfrUploadRequest.File` `files` = 1
  - **File**
    - `string` `name` = 1
- **StartJfrUploadResponse**
  - repeated `lunarclient.websocket.performance.v1.StartJfrUploadResponse.File` `files` = 1
  - `string` `upload_id` = 2
  - `lunarclient.websocket.performance.v1.StartJfrUploadResponse.Status` `status` = 3
  - enum **Status**:
    - `STATUS_UNSPECIFIED = 0`
    - `STATUS_SUCCESS = 1`
    - `STATUS_NOT_ALLOWED = 2`
  - **File**
    - `string` `name` = 1
    - `string` `upload_url` = 2
- **CompleteJfrUploadRequest**
  - `string` `upload_id` = 1
- **CompleteJfrUploadResponse**
