def main():
    deviceCount, fileCount = list(map(int, input().strip().split()))
    result = getTimeFrames(deviceCount, fileCount)
    print(" ".join(map(str, result)))

def getTimeFrames(deviceCount, fileCount):
    totalFileCount = deviceCount * fileCount
    currentFileCount = fileCount
    fileCopyCountByFileNumber = {i:1 for i in range(fileCount)}
    filesByDevice = {i:set() for i in range(deviceCount)}
    filesByDevice[0] = set(range(fileCount))

    devicesByFile = {i:set([0]) for i in range(fileCount)}

    recievedFileCountByDeviceByDevice = {i:{j:0 for j in range(deviceCount)} for i in range(deviceCount)}

    fileDownloadTimeFrameByDevice = {i:-1 for i in range(1, deviceCount)}
    currentTimeFrame = 1
    while currentFileCount < totalFileCount:
        requestedFileByRequestingDevice = {}
        for requestingDevice in range(1, deviceCount):
            filesOnDevice = filesByDevice[requestingDevice]
            if len(filesOnDevice) < fileCount:
                minNumberOfRequestedFileCopyInNetwork = totalFileCount
                for file in range(fileCount):
                    if file not in filesOnDevice and fileCopyCountByFileNumber[file] < minNumberOfRequestedFileCopyInNetwork:
                        requestedFileByRequestingDevice[requestingDevice] = file
                        minNumberOfRequestedFileCopyInNetwork = fileCopyCountByFileNumber[file]
        
        requestedDeviceByRequestingDevice = {}
        for requestingDevice, requestedFile in requestedFileByRequestingDevice.items():
            devicesWithFile = devicesByFile[requestedFile]
            minNumberOfFileCopiesOnRequestedDevice = fileCount + 1
            for requestedDevice in range(deviceCount):
                if requestedDevice in devicesWithFile and len(filesByDevice[requestedDevice]) < minNumberOfFileCopiesOnRequestedDevice:
                    minNumberOfFileCopiesOnRequestedDevice = len(filesByDevice[requestedDevice])
                    requestedDeviceByRequestingDevice[requestingDevice] = requestedDevice
        
        requestingDevicesByRequestedDevice = {}
        for requestingDevice, requestedDevice in requestedDeviceByRequestingDevice.items():
            requestingDevices = requestingDevicesByRequestedDevice.setdefault(requestedDevice, set())
            requestingDevices.add(requestingDevice)

        selectedDeviceByRequestedDevice = {}
        for requestedDevice, requestingDevices in requestingDevicesByRequestedDevice.items():
            maxRecievedFilesFromRequestingDevice = 0
            minFilesOnRequestingDevice = totalFileCount
            recievedFileCountByDevice = recievedFileCountByDeviceByDevice[requestedDevice]
            for requestingDevice in sorted(requestingDevices):
                if maxRecievedFilesFromRequestingDevice < recievedFileCountByDevice[requestingDevice]:
                    minFilesOnRequestingDevice = len(filesByDevice[requestingDevice])
                    selectedDeviceByRequestedDevice[requestedDevice] = requestingDevice
                    maxRecievedFilesFromRequestingDevice = recievedFileCountByDevice[requestingDevice]
                elif (maxRecievedFilesFromRequestingDevice == recievedFileCountByDevice[requestingDevice]
                       and minFilesOnRequestingDevice > len(filesByDevice[requestingDevice])):
                    minFilesOnRequestingDevice = len(filesByDevice[requestingDevice])
                    selectedDeviceByRequestedDevice[requestedDevice] = requestingDevice

        for requestedDevice, selectedDevice in selectedDeviceByRequestedDevice.items():
            transferredFile = requestedFileByRequestingDevice[selectedDevice]

            currentFileCount += 1
            fileCopyCountByFileNumber[transferredFile] += 1
            filesByDevice[selectedDevice].add(transferredFile)
            devicesByFile[transferredFile].add(selectedDevice)
            recievedFileCountByDeviceByDevice[selectedDevice][requestedDevice] += 1

            if len(filesByDevice[selectedDevice]) == fileCount and fileDownloadTimeFrameByDevice[selectedDevice] == -1:
                fileDownloadTimeFrameByDevice[selectedDevice] = currentTimeFrame
        
        currentTimeFrame += 1

    return list(fileDownloadTimeFrameByDevice.values())

if __name__ == '__main__':
    main()    