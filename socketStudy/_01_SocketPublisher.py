#! /usr/bin/python
# -*- coding=utf-8 -*-


"""
向服务器端发送字符串
"""
import socket

class SocketPublisher:

    """
    构造器
    """
    def __init__(self,host="localhost", port=50000):
        self.host = host
        self.port = port

    """
    通过socket发送报文到指定的ip:port 
    """
    def sendMsgBySocket(self):

        # 创建socket连接
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))

        # 发送报文
        s.send("coming from select client ---- ")
        s.send('[stone-runtime] File:"log_writer.py" [2017-05-15 17:16:24,201] line:99 INFO:Streaming: recruit_removal CMD: /home/work/stone_env/hadoop-2.7.1/bin/hadoop jar /home/work/stone_env/hadoop-2.7.1/contrib/streaming/hadoop-streaming-2.7.1.jar -libjars /home/work/stone-framework/lib/multi_path.jar -outputformat com.multipath.MultiPathOutputFormat -jobconf mapred.job.name=hancuiyun::stone_recruit_demo::recruit_removal -mapper "bash ./MAPRED.sh -n recruit_removal -u recruit_removal -m" -reducer "bash ./MAPRED.sh -n recruit_removal -u recruit_removal -r" -jobconf stream.reduce.input.field.separator=    -jobconf mapreduce.job.running.reduce.limit=40 -jobconf mapreduce.reduce.cpu.vcores=4 -jobconf mapred.job.reduce.capacity=200 -jobconf stream.num.map.output.key.fields=3 -jobconf map.output.key.field.separator=     -jobconf mapred.reduce.slowstart.completed.maps=0.8 -jobconf stream.reduce.output=keyonlytext -jobconf mapred.job.map.capacity=200 -jobconf num.key.fields.for.partition=1 -jobconf mapreduce.reduce.memory.mb=4096 -jobconf mapred.min.split.size=512 -jobconf stream.map.output.field.separator=     -jobconf mapred.job.priority=NORMAL -jobconf mapred.textoutputformat.ignoreseparator=true -jobconf mapreduce.map.cpu.vcores=2 -jobconf mapreduce.job.running.map.limit=90 -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner -outputformat org.apache.hadoop.mapred.TextOutputFormat -inputformat org.apache.hadoop.mapred.TextInputFormat -output /user/dy_stone/stone-framework/work/__stone_tmp/recruit_removal_recruit_removal_1494839773_d742ddbb-5cb3-47e7-9534-4c80f94c4db9/ -input /user/dy_export/rawbase_output/dy_recruit_strategy_res/1494836788205/data -cacheArchive /user/dy_stone/airflow/user_dict/recruitment/zhaopin_data_dict.tar.gz#stone_dict -numReduceTasks 400 -file /home/work/stone-framework/src/pyhce/script/MAPRED.sh -file /home/airflow/stone_packages/hancuiyun/recruit_removal/.conf/.recruit_removal_job.json -cacheArchive /user/common/software/python.tar.gz#python -cacheArchive /user/dy_stone/stone-framework/work/01a4a08cf9f936048e091ef771632944/bin.tar.gz#bin -cacheArchive /user/dy_stone/stone-framework/work/01a4a08cf9f936048e091ef771632944/lib.tar.gz#lib')

        s.close()


if __name__ == '__main__':
    thisObj = SocketPublisher()
    thisObj.sendMsgBySocket()