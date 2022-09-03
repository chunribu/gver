from manim import *
from gver import GVer

class Demo(Scene):
    def construct(self):
        dot = Dot().to_corner(UL)
        gver = GVer()

        self.add(gver, dot)
        self.wait()

        gver.add_updater(lambda m: m.watch(dot))
        self.play(dot.animate(run_time=3).to_corner(UR))
        gver.clear_updaters()

        gver.stop_watch()
        gver.wink(self, 2)
        self.wait()

        gver.close_eye(left=True)
        self.wait()