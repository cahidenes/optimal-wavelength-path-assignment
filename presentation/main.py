from manim import *
import random
from manim_slides import Slide
import math

ff = {"font": "Roboto Slab", "color": BLACK, "stroke_color": BLACK}
ff_color = {"font": "Roboto Slab", "stroke_color": BLACK}
graph = None

# path from c f e b
def getpath(path, g=None):
    if g is None:
        g = graph
    path_edges = []
    edges = [(g[path[i]].get_center(), g[path[i+1]].get_center()) for i in range(len(path)-1)]
    for edge in edges:
        path_edges.append(Line(edge[0], edge[1], stroke_width=7))
    path_edges = VGroup(*path_edges)
    return path_edges

class Intro(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"
        # title = Text("Optimal Path Assignment\nFor Wavelength Division\nMultiplexing Networks", font_size=60, font="Roboto Slab", color=WHITE, should_center=True)
        title1 = Text("Optimal Path Assignment", font_size=60, font="Roboto Slab", color=BLACK, stroke_color=BLACK, weight=BOLD)
        title2 = Text("For Wavelength Division", font_size=60, font="Roboto Slab", color=BLACK, stroke_color=BLACK, weight=BOLD)
        title3 = Text("Multiplexing Networks", font_size=60, font="Roboto Slab", color=BLACK, stroke_color=BLACK, weight=BOLD)
        title = VGroup(title1, title2, title3).arrange(DOWN, buff=0.1).move_to(UP*1)

        name = Text("Cahid Enes Keleş", font_size=30, font="Roboto Slab", color=BLUE, stroke_color=BLACK).next_to(title, DOWN, buff=0.5)
        self.play(Write(title), Write(name))

        self.next_slide()

        self.play(Unwrite(title), Unwrite(name))

class WDM(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        node1 = Circle(radius=0.5, color=BLACK, fill_color=WHITE, fill_opacity=1).move_to(LEFT*5)
        node2 = Circle(radius=0.5, color=BLACK, fill_color=WHITE, fill_opacity=1).move_to(RIGHT*5)

        text1 = Text("Node 1", **ff).next_to(node1, DOWN, buff=0.5)
        text2 = Text("Node 2", **ff).next_to(node2, DOWN, buff=0.5)

        self.play(Create(node1), Create(node2), Write(text1), Write(text2))
        self.wait(0.1)

        arrow = Arrow(node1, node2, buff=0.1, color=BLACK)

        self.play(Create(arrow))

        self.next_slide()

        sine = lambda mu: lambda x: 0.5*np.sin(x*mu)
        main_wave = FunctionGraph(sine(4), x_range=[-4, 4], color=BLACK, stroke_width=3)
        self.play(Create(main_wave), FadeOut(arrow))

        self.next_slide()

        group = VGroup(node1, node2, text1, text2, main_wave)
        self.play(group.animate.shift(DOWN*2))

        red = FunctionGraph(sine(2), x_range=[-4, 4], color=RED, stroke_width=3).shift(UP*3)
        green = FunctionGraph(sine(4), x_range=[-4, 4], color=GREEN, stroke_width=3).shift(UP*1.5)
        blue = FunctionGraph(sine(6), x_range=[-4, 4], color=BLUE, stroke_width=3)

        labelred = Text("Channel 1", **ff_color, font_size=20, color=RED).next_to(red, RIGHT, buff=0.5)
        labelgreen = Text("Channel 2", **ff_color, font_size=20, color=GREEN).next_to(green, RIGHT, buff=0.5)
        labelblue = Text("Channel 3", **ff_color, font_size=20, color=BLUE).next_to(blue, RIGHT, buff=0.5)

        self.play(Create(red), Create(green), Create(blue), Write(labelred), Write(labelgreen), Write(labelblue))

        self.next_slide()

        total = FunctionGraph(lambda x: (sine(6)(x) + sine(4)(x) + sine(2)(x))/3, x_range=[-4, 4], color=BLACK, stroke_width=3).shift(DOWN*2)
        self.play(Transform(red, total), FadeOut(labelred), FadeOut(labelgreen), FadeOut(labelblue), Transform(green, total), Transform(blue, total), FadeOut(main_wave))

        self.next_slide()

        self.play(FadeOut(red), FadeOut(green), FadeOut(blue), FadeOut(node1), FadeOut(node2, text1, text2))

class Problem(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Problem Definition", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        random.seed(1)
        names = ["A", "B", "C", "D", "E", "F"]
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 10)
        global graph
        graph = Graph(
            vertices = names,
            edges = edges,
            layout = "kamada_kawai",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )

        self.play(Create(graph), run_time=2)

        self.next_slide()

        self.play(graph.animate.shift(LEFT*3))


        table = Table(
            [["C", "B", '', ''],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)

        table1 = Table(
            [["C", "B", '', ''],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)

        table2 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table2.get_elements()[7].set(color=RED)

        table3 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'FE', 'blue'],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table3.get_elements()[7].set(color=RED)
        table3.get_elements()[11].set(color=BLUE)

        table4 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'FE', 'blue'],
             ["B", "F", 'BEAF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table4.get_elements()[7].set(color=RED)
        table4.get_elements()[11].set(color=BLUE)
        table4.get_elements()[15].set(color=BLUE)

        table6 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", '', ''],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table6.get_elements()[7].set(color=RED)
        table6.get_elements()[15].set(color=BLUE)

        table7 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'EAF', 'red'],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table7.get_elements()[7].set(color=RED)
        table7.get_elements()[11].set(color=RED)
        table7.get_elements()[15].set(color=BLUE)

        table8 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'EAF', 'red'],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", 'CFAD', 'blue'],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table8.get_elements()[7].set(color=RED)
        table8.get_elements()[11].set(color=RED)
        table8.get_elements()[15].set(color=BLUE)
        table8.get_elements()[19].set(color=BLUE)

        label = Text("Number of Available\nWavelengths: 2", **ff, font_size=20, t2c={"2": RED}).next_to(table, DOWN, buff=0.5)
        self.play(Create(table), run_time=2)
        self.next_slide()
        self.play(Write(label))
        self.next_slide()

        self.play(Wiggle(graph), Wiggle(table), Wiggle(label))
        self.next_slide()


        path1 = getpath("CFEB").set_color(RED).shift(UP*0.1)
        path2 = getpath("EF").set_color(BLUE)
        path3 = getpath("BEAF").set_color(BLUE).shift(DOWN*0.1)

        path12 = getpath("CFEB").set_color(RED).shift(UP*0.1)
        path32 = getpath("BEF").set_color(BLUE)
        path22 = getpath("EAF").set_color(RED)
        path4 = getpath("CFAD").set_color(BLUE).shift(DOWN*0.1)

        self.play(Create(path1), Transform(table, table2))
        self.next_slide()
        self.play(Create(path2), Transform(table, table3))
        self.next_slide()
        self.play(Create(path3), Transform(table, table4))
        self.next_slide()

        label2 = Text("# of assigned pairs: 3", **ff, font_size=40, t2c={"3": RED}).move_to(DOWN*3)
        self.play(Write(label2))
        self.next_slide()

        self.play(Uncreate(path1), Uncreate(path2), Uncreate(path3), Unwrite(label2), Transform(table, table1))
        self.next_slide()

        self.play(Create(path12), Transform(table, table2))
        self.next_slide()
        self.play(Create(path32), Transform(table, table6))
        self.next_slide()
        self.play(Create(path22), Transform(table, table7))
        self.next_slide()
        self.play(Create(path4), Transform(table, table8))
        self.next_slide()

        label2 = Text("# of assigned pairs: 4", **ff, font_size=40, t2c={"4": RED}).move_to(DOWN*3)
        self.play(Write(label2))
        self.next_slide()

        self.play(Uncreate(path12), Uncreate(path22), Uncreate(path32), Uncreate(path4), Unwrite(label2), Unwrite(label), Uncreate(table), Uncreate(graph), Unwrite(title), run_time=2)

class Solution(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Solution Mechanism", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        random.seed(1)
        names = ["A", "B", "C", "D", "E", "F"]
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 10)
        global graph
        graph = Graph(
            vertices = names,
            edges = edges,
            layout = "kamada_kawai",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )
        path1 = getpath("CFADEB").set_color(BLUE).shift(DOWN*0.1)
        path2 = getpath("BEAF").set_color(RED).shift(UP*0.1)
        path3 = getpath("EF").set_color(RED).shift(UP*0.1)
        path4 = getpath("CFAEB").set_color(BLUE).shift(DOWN*0.1)
        path5 = getpath("EF").set_color(BLUE).shift(UP*0.1)
        self.play(Create(graph), Create(path1), Create(path2))
        self.next_slide()

        self.play(Uncreate(path2))
        self.next_slide()

        self.play(Create(path3))
        self.next_slide()

        self.play(Transform(path1, path4))
        self.next_slide()
        self.play(Transform(path3, path5))
        self.next_slide()

        group = VGroup(graph, path1, path3)
        self.play(group.animate.shift(LEFT*3))

        svg = SVGMobject("optaPlannerLogo.svg").shift(RIGHT*3.5).scale(0.5)
        self.play(Create(svg), run_time=2)
        self.next_slide()

        self.play(svg.animate.shift(UP*1.5))
        par = Text("Hill Climbing\nTabu Search\nSimulated Annealing\nLate Acceptance\nGreat Deluge\nStep Counting Hill Climbing\nStrategic Oscillation\nVariable Neighborhood Descent", **ff, font_size=25).next_to(svg, DOWN, buff=0.5)
        self.play(Write(par))
        self.next_slide()

        self.play(Uncreate(par), Uncreate(svg), Uncreate(group), Uncreate(title))

class Conclusion(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Thank You For Listening", **ff, font_size=60, weight=BOLD).shift(UP*1)
        self.play(Write(title))
        self.wait(1)
        title = Text("Any Questions?", **ff, font_size=60, weight=BOLD).next_to(title, DOWN, buff=0.5)
        self.play(Write(title))

class Recap(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Quick Recap", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        random.seed(1)
        names = ["A", "B", "C", "D", "E", "F"]
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 10)
        global graph
        graph = Graph(
            vertices = names,
            edges = edges,
            layout = "kamada_kawai",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )

        self.play(Create(graph), run_time=2)

        self.next_slide()

        self.play(graph.animate.shift(LEFT*3))


        table = Table(
            [["C", "B", '', ''],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)

        table1 = Table(
            [["C", "B", '', ''],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)

        table2 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", '', ''],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table2.get_elements()[7].set(color=RED)

        table3 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'FE', 'blue'],
             ["B", "F", '', ''],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table3.get_elements()[7].set(color=RED)
        table3.get_elements()[11].set(color=BLUE)

        table4 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'FE', 'blue'],
             ["B", "F", 'BEAF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table4.get_elements()[7].set(color=RED)
        table4.get_elements()[11].set(color=BLUE)
        table4.get_elements()[15].set(color=BLUE)

        table6 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", '', ''],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table6.get_elements()[7].set(color=RED)
        table6.get_elements()[15].set(color=BLUE)

        table7 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'EAF', 'red'],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", '', ''],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table7.get_elements()[7].set(color=RED)
        table7.get_elements()[11].set(color=RED)
        table7.get_elements()[15].set(color=BLUE)

        table8 = Table(
            [["C", "B", 'CFEB', 'red'],
             ["E", "F", 'EAF', 'red'],
             ["B", "F", 'BEF', 'blue'],
             ["C", "D", 'CFAD', 'blue'],
             ["D", "B", '', '']],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE), Text("Path", **ff_color, color=ORANGE), Text("λ", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*4 + UP*1)
        table8.get_elements()[7].set(color=RED)
        table8.get_elements()[11].set(color=RED)
        table8.get_elements()[15].set(color=BLUE)
        table8.get_elements()[19].set(color=BLUE)

        label = Text("Number of Available\nWavelengths: 2", **ff, font_size=20, t2c={"2": RED}).next_to(table, DOWN, buff=0.5)
        self.play(Create(table), run_time=2)
        self.next_slide()
        self.play(Write(label))
        self.next_slide()

        path1 = getpath("CFEB").set_color(RED).shift(UP*0.1)
        path2 = getpath("EF").set_color(BLUE)
        path3 = getpath("BEAF").set_color(BLUE).shift(DOWN*0.1)

        path12 = getpath("CFEB").set_color(RED).shift(UP*0.1)
        path32 = getpath("BEF").set_color(BLUE)
        path22 = getpath("EAF").set_color(RED)
        path4 = getpath("CFAD").set_color(BLUE).shift(DOWN*0.1)


        self.play(Create(path12), Transform(table, table2))
        self.next_slide()
        self.play(Create(path32), Transform(table, table6))
        self.next_slide()
        self.play(Create(path22), Transform(table, table7))
        self.next_slide()
        self.play(Create(path4), Transform(table, table8))
        self.next_slide()

        label2 = Text("# of assigned pairs: 4", **ff, font_size=40, t2c={"4": RED}).move_to(DOWN*3)
        self.play(Write(label2))
        self.next_slide()

        self.play(Uncreate(path12), Uncreate(path22), Uncreate(path32), Uncreate(path4), Unwrite(label2), Unwrite(label), Uncreate(table), Uncreate(graph), Unwrite(title), run_time=2)


class Moves(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Move Update", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        random.seed(1)
        names = ["A", "B", "C", "D", "E", "F"]
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 10)
        global graph
        graph = Graph(
            vertices = names,
            edges = edges,
            layout = "kamada_kawai",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )
        path1 = getpath("CFADEB").set_color(BLUE).shift(DOWN*0.1)
        path2 = getpath("BEAF").set_color(RED).shift(UP*0.1)
        path3 = getpath("EF").set_color(RED).shift(UP*0.1)
        path4 = getpath("CFA").set_color(BLUE).shift(DOWN*0.1)
        path41 = getpath("CFAE").set_color(BLUE).shift(DOWN*0.1)
        path42 = getpath("CFAD").set_color(BLUE).shift(DOWN*0.1)
        path43 = getpath("CF").set_color(BLUE).shift(DOWN*0.1)
        path45 = getpath("CFA").set_color(RED).shift(DOWN*0.1)

        graph1 = graph.copy()
        graph2 = graph.copy()
        graph3 = graph.copy()
        graph5 = graph.copy()
        graph4 = graph.copy()

        vgroup0 = VGroup(graph, path4)
        vgroup1 = VGroup(graph1, path41)
        vgroup2 = VGroup(graph2, path42)
        vgroup3 = VGroup(graph3, path43)
        vgroup4 = VGroup(graph4)
        vgroup5 = VGroup(graph5, path45)

        self.play(Create(graph), Create(path1), Create(path2))
        self.next_slide()

        self.play(Uncreate(path2))
        self.next_slide()

        self.play(Create(path3))
        self.next_slide()

        self.play(Uncreate(path1), Uncreate(path3))
        self.play(Create(path4))
        self.next_slide()

        vgroup1.shift(LEFT*4).scale(0.8)
        vgroup2.shift(LEFT*4).scale(0.8)
        vgroup3.shift(LEFT*4).scale(0.8)
        vgroup4.shift(LEFT*4).scale(0.8)
        vgroup5.shift(LEFT*4).scale(0.8)
        self.play(vgroup0.animate.shift(LEFT*4).scale(0.8))

        # generate vgroup1 from vgroup0 using an arrow
        arrow1 = Arrow((LEFT*2.5), (RIGHT*0+UP*2), buff=0.1, color=BLACK)
        arrow2 = Arrow((LEFT*2.5), (RIGHT*0+UP*0), buff=0.1, color=BLACK)
        arrow3 = Arrow((LEFT*2.5), (RIGHT*0-UP*2), buff=0.1, color=BLACK)

        self.play(title.animate.shift(LEFT*3))
        self.play(vgroup1.animate.shift(RIGHT*5+UP*2).scale(0.5))
        self.play(vgroup2.animate.shift(RIGHT*8+UP*2).scale(0.5))
        self.play(Create(arrow1))
        self.next_slide()

        self.play(vgroup3.animate.shift(RIGHT*5+UP*0).scale(0.5))
        self.play(vgroup4.animate.shift(RIGHT*8-UP*0).scale(0.5))
        self.play(Create(arrow2))
        self.next_slide()

        self.play(vgroup5.animate.shift(RIGHT*6.5-UP*2).scale(0.5))
        self.play(Create(arrow3))
        self.next_slide()

        self.play(Uncreate(arrow1), Uncreate(arrow2), Uncreate(arrow3), Uncreate(vgroup1), Uncreate(vgroup2), Uncreate(vgroup3), Uncreate(vgroup4), Uncreate(vgroup5), Unwrite(title), Uncreate(vgroup0))

class Score(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Score", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        score = Text("??hard/??medium/??soft", **ff, font_size=40, t2c={'?': RED})
        score1 = Text("-2hard/??medium/??soft", **ff, font_size=40, t2c={'?': RED, '-2': RED})
        score2 = Text("-2hard/+2medium/??soft", **ff, font_size=40, t2c={'?': RED, '-2': RED, '+2': RED})
        score3 = Text("-2hard/+2medium/-3soft", **ff, font_size=40, t2c={'?': RED, '-2': RED, '+2': RED, '-3': RED})
        scores = [score1, score2, score3]

        self.play(Write(score))
        self.next_slide()
        self.play(score.animate.shift(RIGHT*3+UP*1.5))
        for s in scores:
            s.shift(RIGHT*3+UP*1.5)

        random.seed(1)
        names = ["A", "B", "C", "D", "E", "F"]
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 10)
        global graph
        graph = Graph(
            vertices = names,
            edges = edges,
            layout = "kamada_kawai",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )
        graph.shift(LEFT*3)

        table = Table(
            [["C", "B"],
             ["B", "F"],
             ["A", "E"],
             ["C", "D"]],
            col_labels=[Text("Src", **ff_color, color=ORANGE), Text("Dst", **ff_color, color=ORANGE)],
            line_config={"color": BLACK},
            element_to_mobject_config={"color": BLACK, "stroke_color": BLACK},
        ).scale(0.5).shift(RIGHT*3 + DOWN*1)

        path1 = getpath("CFAD").set_color(BLUE).shift(DOWN*0.1)
        path2 = getpath("FADEB").set_color(BLUE).shift(UP*0.1)
        path3 = getpath("CF").set_color(RED).shift(UP*0.1)

        self.play(Create(graph), Create(table), Create(path1), Create(path2), Create(path3))
        self.next_slide()

        self.play(Transform(score, score1))
        self.next_slide()

        self.play(Transform(score, score2))
        self.next_slide()

        self.play(Transform(score, score3))
        self.next_slide()

        self.play(Uncreate(graph), Uncreate(table), Uncreate(path1), Uncreate(path2), Uncreate(path3), Uncreate(score), Uncreate(title))


class OptimizationMethod(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Optimization Method", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        t0 = Text("Hill Climbing", **ff_color, color=BLUE, font_size=30).shift(UP*2)
        t1 = Text("Tabu Search", **ff_color, color=BLUE, font_size=30).shift(UP*1.5)
        t2 = Text("Variable Neightborhood Descent", **ff_color, color=BLUE, font_size=30).shift(UP*1)
        t3 = Text("Simulated Annealing", **ff_color, color=BLUE, font_size=30).shift(UP*0.5)
        t4 = Text("Late Acceptance", **ff_color, color=BLUE, font_size=30).shift(UP*0)
        t5 = Text("Great Deluge", **ff_color, color=BLUE, font_size=30).shift(DOWN*0.5)
        t6 = Text("Step Counting Hill Climbing", **ff_color, color=BLUE, font_size=30).shift(DOWN*1)
        t7 = Text("Strategic Oscillation", **ff_color, color=BLUE, font_size=30).shift(DOWN*1.5)

        self.play(Write(t0))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(Write(t7))
        self.next_slide()

        self.play(t7.animate.shift(DOWN*0.5).scale(2))
        self.next_slide()

        self.play(FadeOut(t0), FadeOut(t1), FadeOut(t2), FadeOut(t3), FadeOut(t4), FadeOut(t5), FadeOut(t6), FadeOut(title), t7.animate.shift(UP*5))
        t0 = Text("Current Score: -3hard/+4medium/-5soft", **ff, font_size=30, t2c={"-3": RED, "+4": RED, "-5": RED}).shift(UP*2)
        t1 = Text("Possible Moves:", **ff, font_size=30, weight=BOLD, t2c={"-3": RED, "+4": RED, "-5": RED}).shift(UP*0.7)
        m0 = Text("-4hard/+3medium/-5soft", **ff, font_size=25, t2c={"-4": RED, "+3": RED, "-5": RED}).shift(UP*0)
        m1 = Text("-5hard/+5medium/-5soft", **ff, font_size=25, t2c={"-5": RED, "+5": RED, "-5": RED}).shift(-UP*0.5)
        m2 = Text("-6hard/+7medium/-5soft", **ff, font_size=25, t2c={"-6": RED, "+7": RED, "-5": RED}).shift(-UP*1)


        self.play(Write(t0))
        self.next_slide()

        self.play(Write(t1), Write(m0), Write(m1), Write(m2))
        self.next_slide()

        self.play(Wiggle(m2))
        self.next_slide()

        self.play(Unwrite(t0), Unwrite(t1), Unwrite(m0), Unwrite(m1), Unwrite(m2), Unwrite(t7))


class Tests(Slide):
    def construct(self):
        self.camera.background_color = "#FFFFFF"

        title = Text("Tests", **ff, font_size=60, weight=BOLD)
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.shift(UP*3.3).scale(0.7))

        random.seed(1)
        names = list("ABCDEFGHIJKLMNOP")
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 16*3)
        sparse = Graph(
            vertices = names,
            edges = edges,
            layout = "spring",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )
        sparse.shift(LEFT*3).scale(0.8)
        sparse_paths = [getpath(random.sample(names, random.randint(1, 5)), sparse).set_color(random.choice([RED, BLUE, GREEN])) for _ in range(4)]

        names = list("ABCDEFGHIJKLMNOP")
        edges = random.sample([(names[x], names[y]) for x in range(len(names)) for y in range(len(names)) if x != y], 16*3)
        dense = Graph(
            vertices = names,
            edges = edges,
            layout = "spring",
            edge_config = {"color": BLACK, "stroke_color": BLACK},
            vertex_config = {"color": BLACK, "stroke_color": BLACK, "radius": 0.3},
            labels=True,
            label_fill_color = WHITE,
            layout_scale = 3
        )
        dense.shift(RIGHT*3).scale(0.8)
        dense_paths = [getpath(random.sample(names, random.randint(3, 7)), dense).set_color(random.choice([RED, BLUE, GREEN])) for _ in range(15)]

        self.play(Create(sparse), run_time=1)
        self.play(*[Create(path) for path in sparse_paths], run_time=2)
        self.play(sparse.animate.shift(DOWN), *[path.animate.shift(DOWN) for path in sparse_paths], run_time=1)
        sparse_text = Text("Sparse Graph", **ff_color, color=RED, font_size=30).move_to(LEFT*3 + UP*2)
        self.play(Write(sparse_text))
        self.next_slide()

        self.play(Create(dense), run_time=1)
        self.play(*[Create(path) for path in dense_paths], run_time=2)
        self.play(dense.animate.shift(DOWN), *[path.animate.shift(DOWN) for path in dense_paths], run_time=1)
        dense_text = Text("Dense Graph", **ff_color, color=RED, font_size=30).move_to(RIGHT*3 + UP*2)
        self.play(Write(dense_text))
        self.next_slide()

        self.play(FadeOut(sparse), *[FadeOut(path) for path in sparse_paths])
        t0 = Text("Measure Time", **ff, font_size=30).next_to(sparse_text, DOWN, buff=0.5)
        t1 = Text("Vs Integer Programming", **ff, font_size=30).next_to(t0, DOWN, buff=0.1)
        t2 = Text("Optimal Value", **ff_color, color=BLUE, font_size=30).next_to(t1, DOWN, buff=0.1)
        t3 = Text("(R. Ramaswami and K. N. Sivarajan, 1994)", **ff, font_size=15).next_to(t2, DOWN, buff=0.1)
        self.play(Write(t0), Write(t1), Write(t2), Write(t3))
        self.next_slide()

        self.play(FadeOut(dense), *[FadeOut(path) for path in dense_paths])
        t4 = Text("Measure Objective Function", **ff, font_size=30).next_to(dense_text, DOWN, buff=0.5)
        t5 = Text("Vs IP Relaxation", **ff, font_size=30).next_to(t4, DOWN, buff=0.1)
        t6 = Text("Upper Bound", **ff_color, color=BLUE, font_size=30).next_to(t5, DOWN, buff=0.1)
        t7 = Text("(R. Ramaswami and K. N. Sivarajan, 1994)", **ff, font_size=15).next_to(t6, DOWN, buff=0.1)
        self.play(Write(t4), Write(t5), Write(t6), Write(t7))
        self.next_slide()

        self.play(FadeOut(title), FadeOut(dense_text), FadeOut(sparse_text), FadeOut(t0), FadeOut(t2), FadeOut(t3), FadeOut(t4), FadeOut(t5), FadeOut(t6), FadeOut(t7), t1.animate.shift(UP*2.5+RIGHT*3).scale(1.4))
        t5.shift(UP*2.5+LEFT*3).scale(1.4)
        
        sizes = [5, 7, 10, 15, 20, 30, 40, 50, 60, 70, 100, 120, 150, 200, 300, 500, 1000]
        ip = [0.038549423, 0.073654175, 0.163833618, 0.565175533, 1.685163736, 10.59370661, 39.25944972, 106.442312, 771.6668482, 1902.427092]
        my = [0.096086924, 0.098097872, 0.066622182, 0.076427751, 0.095681182, 0.129287211, 0.21919474, 0.266737023, 0.331661646, 0.380001521, 0.710284962, 0.685508056, 1.738074609, 1.656067866, 4.448157723, 46.67746015, 58.45901861]
        ax = Axes(
                x_range=[0, 75, 5],
                y_range=[-2, 3, 1],
                tips=False,
                axis_config={"color": BLACK, "include_numbers": True},
                y_axis_config={"scaling": LogBase()}
                )
        labels = ax.get_axis_labels(
                Text("Input Size", color=BLACK, font_size=20),
                Text("Time (s)", color=BLACK, font_size=20),
                )
        for tick in ax.y_axis.labels:
            tick.set_color(BLACK)
        for tick in ax.x_axis.numbers:
            tick.set_color(BLACK)

        plot = ax.plot_line_graph(x_values=sizes[:len(ip)], y_values=ip, line_color=BLUE, vertex_dot_style={"stroke_width":3,"fill_color":BLUE})

        self.play(Create(ax), Write(labels), run_time=2)
        self.play(Create(plot), run_time=2)
        self.next_slide()

        plot2 = ax.plot_line_graph(x_values=sizes, y_values=my, line_color=RED, vertex_dot_style={"stroke_width":3,"fill_color":RED})
        self.play(Create(plot2), run_time=2)
        self.next_slide()

        ax2 = Axes(
                x_range=[0, 75*14, 100],
                y_range=[-2, 3, 1],
                tips=False,
                axis_config={"color": BLACK, "include_numbers": True},
                y_axis_config={"scaling": LogBase()}
                )
        for tick in ax2.y_axis.labels:
            tick.set_color(BLACK)
        for tick in ax2.x_axis.numbers:
            tick.set_color(BLACK)

        plot12 = ax2.plot_line_graph(x_values=sizes[:len(ip)], y_values=ip, line_color=BLUE, vertex_dot_style={"stroke_width":3,"fill_color":BLUE})
        plot22 = ax2.plot_line_graph(x_values=sizes, y_values=my, line_color=RED, vertex_dot_style={"stroke_width":3,"fill_color":RED})

        # scale plot2 only on x
        self.play(Transform(ax, ax2), Transform(plot, plot12), Transform(plot2, plot22), run_time=2)
        self.next_slide()

        self.play(Uncreate(plot), Uncreate(plot2), Uncreate(ax), Uncreate(labels), Unwrite(t1), run_time=2)


        sizes = [3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 25, 30, 35, 40, 45, 50, 60, 70, 100, 120, 150, 200, 300, 500, 1000]
        ip = [17, 30, 32, 39, 42, 43, 51, 56, 62, 74.00000001, 79.00000002, 86.19999997, 116.0000001, 126.375, 132.1666667, 146.0416667, 162.7, 171.1319444, 198.0454546, 229.4651162]
        ops = [17, 30, 32, 39, 42, 43, 51, 56, 62, 74, 79, 86, 115]
        my = [10, 25, 27, 30, 26, 31, 38, 34, 38, 45, 45, 39, 58, 54, 53, 53, 63, 67, 72, 80, 92, 97, 100, 117, 145, 172, 233]

        ax = Axes(
                x_range=[0, 75, 5],
                y_range=[0, 250, 50],
                tips=False,
                axis_config={"color": BLACK, "include_numbers": True},
                )
        labels = ax.get_axis_labels(
                Text("Input Size", color=BLACK, font_size=20),
                Text("Objective Function", color=BLACK, font_size=20),
                )
        for tick in ax.y_axis.numbers:
            tick.set_color(BLACK)
        for tick in ax.x_axis.numbers:
            tick.set_color(BLACK)

        plot = ax.plot_line_graph(x_values=sizes[:len(ip)], y_values=ip, line_color=BLUE, vertex_dot_style={"stroke_width":3,"fill_color":BLUE})

        self.play(Write(t5))
        self.play(Create(ax), Write(labels), run_time=2)
        self.play(Create(plot), run_time=2)
        self.next_slide()

        plot2 = ax.plot_line_graph(x_values=sizes, y_values=my, line_color=RED, vertex_dot_style={"stroke_width":3,"fill_color":RED})
        self.play(Create(plot2), run_time=2)
        self.next_slide()

        plot3 = ax.plot_line_graph(x_values=sizes[:len(ops)], y_values=ops, line_color=GREEN, vertex_dot_style={"stroke_width":3,"fill_color":GREEN})
        self.play(Create(plot3), run_time=2)
        self.next_slide()

        ax2 = Axes(
                x_range=[0, 75*14, 100],
                y_range=[0, 250, 50],
                tips=False,
                axis_config={"color": BLACK, "include_numbers": True},
                )
        for tick in ax2.y_axis.numbers:
            tick.set_color(BLACK)
        for tick in ax2.x_axis.numbers:
            tick.set_color(BLACK)

        plot12 = ax2.plot_line_graph(x_values=sizes[:len(ip)], y_values=ip, line_color=BLUE, vertex_dot_style={"stroke_width":3,"fill_color":BLUE})
        plot22 = ax2.plot_line_graph(x_values=sizes, y_values=my, line_color=RED, vertex_dot_style={"stroke_width":3,"fill_color":RED})
        plot32 = ax2.plot_line_graph(x_values=sizes[:len(ops)], y_values=ops, line_color=GREEN, vertex_dot_style={"stroke_width":3,"fill_color":GREEN})

        # scale plot2 only on x
        self.play(Transform(ax, ax2), Transform(plot, plot12), Transform(plot2, plot22), Transform(plot3, plot32), run_time=2)
        self.next_slide()

        self.play(Uncreate(plot), Uncreate(plot2), Uncreate(ax), Uncreate(labels), Unwrite(t5), run_time=2)
