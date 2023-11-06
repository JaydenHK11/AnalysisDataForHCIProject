using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class TimeToReachTargets : MonoBehaviour
{
    public Transform flowPoint;
    public string csvFilePath = "Assets/PointData.csv"; 
    public float minTimeBetweenTouches = 0.1f; 
    public GameObject[] excludedGameObjects; 

    private float lastTouchTime = 0f;
    private List<string> recordedData = new List<string>();

    private void Update()
    {
        Collider[] colliders = Physics.OverlapSphere(flowPoint.position, 0.1f); 

        foreach (Collider collider in colliders)
        {
            
            if (!IsExcluded(collider.gameObject) && Time.time - lastTouchTime >= minTimeBetweenTouches)
            {
                // 当flowPoint触碰到不在排除列表中的游戏对象时记录时间点
                lastTouchTime = Time.time;
                string dataLine = $"{collider.gameObject.name},{Time.time:F2}";
                recordedData.Add(dataLine);
                Debug.Log("FlowPoint reached " + collider.gameObject.name + " at " + Time.time.ToString("F2"));
            }
        }
    }

    private bool IsExcluded(GameObject obj)
    {
        // 检查游戏对象是否在排除列表中
        foreach (GameObject excludedObj in excludedGameObjects)
        {
            if (obj == excludedObj)
            {
                return true;
            }
        }
        return false;
    }

    private void OnApplicationQuit()
    {
        // 保存数据到CSV文件
        SaveDataToFile();
    }

    private void SaveDataToFile()
    {
        using (StreamWriter sw = File.CreateText(csvFilePath))
        {
            sw.WriteLine("GameObjectName,Time");

            foreach (string dataLine in recordedData)
            {
                sw.WriteLine(dataLine);
            }
        }
    }
}
