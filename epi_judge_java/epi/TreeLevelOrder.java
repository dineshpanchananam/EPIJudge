package epi;
import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

import java.util.List;

import java.util.LinkedList;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;


public class TreeLevelOrder {
  @EpiTest(testDataFile = "tree_level_order.tsv")

  public static List<List<Integer>>
  binaryTreeDepthOrder(BinaryTreeNode<Integer> tree) {
	  
	  List<BinaryTreeNode<Integer>> stack = new ArrayList<>();
	  List<BinaryTreeNode<Integer>> stack2;
	  stack.add(tree);
	  
	  List<List<Integer>> answer = new ArrayList<>();
	  
	  while (!stack.isEmpty()) {
		  List<Integer> thisLevel = new ArrayList<>();
		  stack2 = new ArrayList<>();
		  for (var node: stack) {
			  if (node != null) {
				  thisLevel.add(node.data);
				  stack2.add(node.left);
				  stack2.add(node.right);
			  }
		  }
		  if (!thisLevel.isEmpty()) {
			  answer.add(thisLevel);
		  }
		  stack = stack2;
	  }
	  
	  return answer;
  }

  public static void main(String[] args) {
    System.exit(
        GenericTest
            .runFromAnnotations(args, "TreeLevelOrder.java",
                                new Object() {}.getClass().getEnclosingClass())
            .ordinal());
  }
}
