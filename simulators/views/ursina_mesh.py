# -*- coding:utf-8 -*-
# title           :ursina天体视图
# description     :ursina天体视图（天体效果展示用，需要安装 ursina）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, Mesh, EditorCamera, color, mouse, Vec2, Vec3, load_texture,Texture
from math import pi, sin, cos
import numpy as np
import math


def create_sphere(radius, subdivisions):
    """
    创建一个球体
    :param radius:
    :param subdivisions:
    :return:
    """
    # 生成球体的顶点、UV坐标uvs、法线tris和三角面
    verts = []
    tris = []
    normals = []
    uvs = []

    for y in range(subdivisions + 1):
        for x in range(subdivisions + 1):
            x_segment = x / subdivisions
            y_segment = -y / subdivisions
            x_pos = cos(x_segment * 2 * pi) * sin(y_segment * pi)
            y_pos = cos(y_segment * pi)
            z_pos = sin(x_segment * 2 * pi) * sin(y_segment * pi)

            verts.append(Vec3(x_pos, y_pos, z_pos) * radius)
            uvs.append(Vec2(x_segment, y_segment))
            normals.append(Vec3(x_pos, y_pos, z_pos))

    for y in range(subdivisions):
        for x in range(subdivisions):
            first = (y * (subdivisions + 1)) + x
            second = first + subdivisions + 1
            # tris.append((first, second + 1, second))
            # tris.append((first, first + 1, second + 1))

            tris.append((second, second + 1, first))
            tris.append((second + 1, first + 1, first))

    # 反转面法线
    # for i in range(len(tris)):
    #     a, b, c = tris[i]
    #     tris[i] = (c, b, a)
    #     normals[a], normals[b], normals[c] = -Vec3(*normals[c]), -Vec3(*normals[b]), -Vec3(*normals[a])
    # normals[a], normals[b], normals[c] = -Vec3(*normals[a]), -Vec3(*normals[b]), -Vec3(*normals[c])
    # 翻转球体
    # for i in range(len(normals)):
    #     normals[i] = -normals[i]

    return Mesh(vertices=verts, triangles=tris, normals=normals, uvs=uvs, mode='triangle')


def create_body_torus(inner_radius, outer_radius, subdivisions):
    vertices = []
    uvs = []
    normals = []
    triangles = []

    # 计算圆环顶点、法向量和纹理坐标
    for i in range(subdivisions):
        for j in range(subdivisions):
            # 计算纹理坐标
            u = i / subdivisions
            v = j / subdivisions
            # 计算球面坐标系下的角度
            theta = u * math.pi * 2
            phi = v * math.pi * 2

            # 计算圆环顶点位置
            x = (outer_radius + inner_radius * math.cos(phi)) * math.cos(theta)
            y = inner_radius * math.sin(phi) * (inner_radius / 20)
            z = (outer_radius + inner_radius * math.cos(phi)) * math.sin(theta)

            # 计算圆环顶点法向量
            nx = math.cos(theta) * math.cos(phi)
            ny = math.sin(phi)
            nz = math.sin(theta) * math.cos(phi)

            vertices.append((x, y, z))
            normals.append((nx, ny, nz))
            uvs.append((u, v))

    # 计算圆环三角形面片
    for i in range(subdivisions):
        for j in range(subdivisions):
            i1 = i
            j1 = j
            i2 = (i + 1) % subdivisions
            j2 = (j + 1) % subdivisions

            p1 = i1 * subdivisions + j1
            p2 = i2 * subdivisions + j1
            p3 = i2 * subdivisions + j2
            p4 = i1 * subdivisions + j2

            triangles.append((p1, p2, p3))
            triangles.append((p1, p3, p4))
    # uvs = [[u * 2, v] for u, v in uvs]
    # 创建 mesh 对象
    mesh = Mesh(vertices=vertices, uvs=uvs, normals=normals, triangles=triangles, mode='triangle')

    return mesh


def create_torus(inner_radius, outer_radius, subdivisions):
    verts = []
    tris = []

    for i in range(subdivisions):
        angle = i * (360 / subdivisions)
        x = np.cos(angle * np.pi / 180)
        y = np.sin(angle * np.pi / 180)

        # create vertices for inner radius
        inner_x = x * inner_radius
        inner_y = y * inner_radius
        verts.append((inner_x, inner_y, 0))

        # create vertices for outer radius
        outer_x = x * outer_radius
        outer_y = y * outer_radius
        verts.append((outer_x, outer_y, 0))

        # create triangles
        first_index = i * 2
        second_index = (i * 2 + 2) % (subdivisions * 2)
        third_index = (i * 2 + 1) % (subdivisions * 2)
        fourth_index = (i * 2 + 3) % (subdivisions * 2)

        tris.append((first_index, second_index, third_index))
        tris.append((third_index, second_index, fourth_index))

    # create uvs
    uvs = []
    # for i in range(len(verts)):
    #     # 计算纹理坐标
    #     u = -i / subdivisions
    #     v = i / subdivisions
    #
    #     # angle = i * (360 / (subdivisions * 2))
    #     # u = -angle / 360
    #     # v = angle / 360
    #
    #
    #     # angle = i * (360 / (subdivisions * 2))
    #     # u = angle / 360
    #     # v = -(outer_radius - inner_radius) / outer_radius * 0.5
    #     uvs.append((u, v))
    uvs = []
    # for i in range(len(verts)):
    #     angle = i * (360 / (subdivisions * 2))
    #     u = angle / 360
    #     phi = u * 2 * math.pi
    #     v = phi / (2 * math.pi)
    #     uvs.append((u, v))
    # for i in range(len(verts)):
    #     angle = i * (360 / (subdivisions * 2))
    #     u = (outer_radius + inner_radius * math.cos(angle)) / (2 * outer_radius)
    #     v = i / len(verts)
    #     uvs.append((u, v))
    for i in range(len(verts)):
        angle = i * (360 / (subdivisions * 2))
        u = (outer_radius + inner_radius * math.cos(angle)) / (2 * outer_radius)
        v = i / len(verts)
        uvs.append((v, 1 - u))
    # uvs = []
    # for i in range(subdivisions):
    #     for j in range(subdivisions):
    #         u = i / subdivisions
    #         v = j / subdivisions
    #         uvs.append((u, v))
            # uvs.append((v, 1 - u))
    # uvs= []
    # for i in range(subdivisions):
    #     theta = i * 2 * math.pi / subdivisions
    #     for j in range(subdivisions):
    #         phi = j * 2 * math.pi / subdivisions
    #         u = i / subdivisions * 2
    #         v = j / subdivisions
    #         uvs.append((u, v))

    # uvs = [(u, v /0) for u, v in uvs]
    # create normals
    normals = []
    for i in range(len(verts)):
        angle = i * (360 / subdivisions)
        x = np.cos(angle * np.pi / 180)
        y = np.sin(angle * np.pi / 180)
        normals.append((x, y, 0))

    # create mesh
    mesh = Mesh(vertices=verts, triangles=tris, uvs=uvs, normals=normals, mode='triangle')

    # add color attribute
    # mesh.colorize()

    return mesh


if __name__ == '__main__':
    app = Ursina()
    # # 使用 Mesh 类创建球体
    texture = "../../textures/saturn.jpg"
    textureRings = '../../textures/saturnRings.jpg'

    # 创建球体
    sphere = create_sphere(1, 32)
    entity = Entity(model=sphere, texture=texture, color=color.white)
    # 创建光晕
    # glow_entity = Entity(parent=entity, model='sphere', color=color.rgb(1,1,1,0.1),
    #                      scale=2.1, alpha=0.1)
    #



    # torus = create_body_torus(0.8, 2, 64)
    # textureRings = load_texture(textureRings)
    # entity = Entity(model=torus, texture=textureRings, rotation=(0, 0, 0), double_sided=True)



    torus = create_torus(1.5, 3, 64)
    entity = Entity(model=torus, texture=textureRings, rotation=(85, 0, 0), double_sided=True)


    EditorCamera()
    app.run()
