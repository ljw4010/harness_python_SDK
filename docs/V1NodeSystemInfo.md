# V1NodeSystemInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine_id** | **str** |  | [optional] 
**system_uuid** | **str** |  | [optional] 
**boot_id** | **str** | Boot ID reported by the node. | [optional] 
**kernel_version** | **str** | Kernel Version reported by the node from &#x27;uname -r&#x27; (e.g. 3.16.0-0.bpo.4-amd64). | [optional] 
**os_image** | **str** | OS Image reported by the node from /etc/os-release (e.g. Debian GNU/Linux 7 (wheezy)). | [optional] 
**container_runtime_version** | **str** | ContainerRuntime Version reported by the node through runtime remote API (e.g. docker://1.5.0). | [optional] 
**kubelet_version** | **str** | Kubelet Version reported by the node. | [optional] 
**kube_proxy_version** | **str** | KubeProxy Version reported by the node. | [optional] 
**operating_system** | **str** |  | [optional] 
**architecture** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

