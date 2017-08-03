/*
Copyright (c) 2010-2016, Mathieu Labbe - IntRoLab - Universite de Sherbrooke
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Universite de Sherbrooke nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

#ifndef UTIL3D_TRANSFORMS_H_
#define UTIL3D_TRANSFORMS_H_

#include <rtabmap/core/RtabmapExp.h>

#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/pcl_base.h>
#include <rtabmap/core/Transform.h>

namespace rtabmap
{

namespace util3d
{

cv::Mat RTABMAP_EXP transformLaserScan(
		const cv::Mat & laserScan,
		const Transform & transform);

pcl::PointCloud<pcl::PointXYZ>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZ>::Ptr & cloud,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZ>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZ>::Ptr & cloud,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZRGB>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZRGB>::Ptr & cloud,
		const Transform & transform);
pcl::PointCloud<pcl::PointNormal>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointNormal>::Ptr & cloud,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZRGBNormal>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZRGBNormal>::Ptr & cloud,
		const Transform & transform);

pcl::PointCloud<pcl::PointXYZ>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZ>::Ptr & cloud,
		const pcl::IndicesPtr & indices,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZ>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZ>::Ptr & cloud,
		const pcl::IndicesPtr & indices,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZRGB>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZRGB>::Ptr & cloud,
		const pcl::IndicesPtr & indices,
		const Transform & transform);
pcl::PointCloud<pcl::PointNormal>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointNormal>::Ptr & cloud,
		const pcl::IndicesPtr & indices,
		const Transform & transform);
pcl::PointCloud<pcl::PointXYZRGBNormal>::Ptr RTABMAP_EXP transformPointCloud(
		const pcl::PointCloud<pcl::PointXYZRGBNormal>::Ptr & cloud,
		const pcl::IndicesPtr & indices,
		const Transform & transform);

cv::Point3f RTABMAP_EXP transformPoint(
		const cv::Point3f & pt,
		const Transform & transform);
pcl::PointXYZ RTABMAP_EXP transformPoint(
		const pcl::PointXYZ & pt,
		const Transform & transform);
pcl::PointXYZRGB RTABMAP_EXP transformPoint(
		const pcl::PointXYZRGB & pt,
		const Transform & transform);
pcl::PointNormal RTABMAP_EXP transformPoint(
		const pcl::PointNormal & point,
		const Transform & transform);
pcl::PointXYZRGBNormal RTABMAP_EXP transformPoint(
		const pcl::PointXYZRGBNormal & point,
		const Transform & transform);

} // namespace util3d
} // namespace rtabmap

#endif /* UTIL3D_TRANSFORMS_H_ */