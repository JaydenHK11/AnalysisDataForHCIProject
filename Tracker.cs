using System.Collections.Generic;
using UnityEngine;
using Valve.VR;
using System.IO;

namespace Valve.VR
{
    public class TrackerRecorder : MonoBehaviour
    {
        public SteamVR_TrackedObject[] trackers;
        public bool[] recordFlags;
        public string outputFolderPath = "Assets/";

        private List<List<string>> dataLinesList = new List<List<string>>();
        private Vector3[] lastPositions;
        private float[] lastRecordTimes;

        private void Start()
        {
            recordFlags = new bool[trackers.Length];
            lastPositions = new Vector3[trackers.Length];
            lastRecordTimes = new float[trackers.Length];

            for (int i = 0; i < trackers.Length; i++)
            {
                recordFlags[i] = false;
                dataLinesList.Add(new List<string>());
                dataLinesList[i].Add("Time,TrackerIndex,PositionX,PositionY,PositionZ,VelocityX,VelocityY,VelocityZ");
            }

            SteamVR_Events.NewPoses.AddListener(OnNewPoses);
        }

        private void OnNewPoses(TrackedDevicePose_t[] poses)
        {
            for (int i = 0; i < trackers.Length; i++)
            {
                if (trackers[i].index != SteamVR_TrackedObject.EIndex.None && recordFlags[i])
                {
                    int index = (int)trackers[i].index;

                    if (poses.Length <= index || !poses[index].bDeviceIsConnected)
                        continue;

                    if (!poses[index].bPoseIsValid)
                        continue;

                    var pose = new SteamVR_Utils.RigidTransform(poses[index].mDeviceToAbsoluteTracking);

                    float deltaTime = Time.time - lastRecordTimes[i];
                    Vector3 position = trackers[i].origin != null ?
                        trackers[i].origin.transform.TransformPoint(pose.pos) :
                        pose.pos;

                    if (lastRecordTimes[i] > 0f && deltaTime > 0f)
                    {
                        Vector3 positionDiff = position - lastPositions[i];
                        positionDiff *= 1000f;

                        Vector3 velocity = positionDiff / deltaTime;

                        string dataLine = $"{Time.time},{i},{position.x},{position.y},{position.z},{velocity.x},{velocity.y},{velocity.z}";

                        dataLinesList[i].Add(dataLine);
                    }

                    lastPositions[i] = position;
                    lastRecordTimes[i] = Time.time;
                }
            }
        }

        private void OnApplicationQuit()
        {
            for (int i = 0; i < trackers.Length; i++)
            {
                SaveDataToFile(i);
            }
        }

        public void SaveDataToFile(int trackerIndex)
        {
            if (trackerIndex < 0 || trackerIndex >= trackers.Length)
                return;

            string filePath = Path.Combine(outputFolderPath, $"TrackerData{trackerIndex}.csv");
            File.WriteAllLines(filePath, dataLinesList[trackerIndex].ToArray());
        }
    }
}
